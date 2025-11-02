import requests
import time
import csv
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# === CONFIG ===
INPUT = "post_numbers.txt"
OUTPUT = "addfav_results.csv"
COOKIE_STRING = "gdpr=1; gdpr-consent=1; user_id=5487729; pass_hash=... (met ton cookie)"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "*/*",
    "Referer": "https://rule34.xxx/index.php?page=post&s=view&id=3024475",
    "Cookie": COOKIE_STRING
}
BASE_URL = "https://rule34.xxx/public/addfav.php?id={}"

# Contrôle de la vitesse (req/s cible)
TARGET_RPS = 1.5   # ~15 000 requêtes en ~2h45
MAX_WORKERS = 6    # threads
MAX_RETRIES = 3
TIMEOUT = 15
JITTER = 0.25      # variation aléatoire

# === Rate limiter (token bucket) ===
class TokenBucket:
    def __init__(self, rate):
        self.rate = rate
        self.capacity = rate * 2
        self._tokens = self.capacity
        self._last = time.monotonic()
        self._lock = threading.Lock()

    def consume(self, tokens=1):
        while True:
            with self._lock:
                now = time.monotonic()
                delta = now - self._last
                if delta > 0:
                    self._tokens = min(self.capacity, self._tokens + delta * self.rate)
                    self._last = now
                if self._tokens >= tokens:
                    self._tokens -= tokens
                    return
                need = (tokens - self._tokens) / self.rate
            time.sleep(max(need * 0.9, 0.05))

# === worker ===
def do_request(session, pid, rate_limiter):
    url = BASE_URL.format(pid)
    rate_limiter.consume()
    time.sleep(random.uniform(0, JITTER))
    tries = 0
    while tries <= MAX_RETRIES:
        tries += 1
        try:
            r = session.get(url, headers=HEADERS, timeout=TIMEOUT)
            status = r.status_code
            if status == 200:
                print(f"→ ID {pid}: OK (200)")
                return (pid, 200, "")
            if status in (429, 503) and tries <= MAX_RETRIES:
                print(f"→ ID {pid}: {status}, retry {tries}/{MAX_RETRIES}")
                backoff = (2 ** (tries - 1)) + random.random()
                time.sleep(backoff)
                continue
            print(f"→ ID {pid}: HTTP {status}")
            return (pid, status, f"HTTP {status}")
        except requests.RequestException as e:
            if tries <= MAX_RETRIES:
                print(f"→ ID {pid}: erreur {e}, retry {tries}/{MAX_RETRIES}")
                backoff = (2 ** (tries - 1)) + random.random()
                time.sleep(backoff)
                continue
            print(f"→ ID {pid}: échec définitif ({e})")
            return (pid, None, str(e))

# === main ===
def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        ids = [line.strip() for line in f if line.strip()]
    total = len(ids)
    if total == 0:
        print("Aucun ID trouvé.")
        return

    est_seconds = total / TARGET_RPS
    print(f"{total} IDs — cadence {TARGET_RPS:.2f} req/s → ~{est_seconds/3600:.2f} h estimées")

    rate_limiter = TokenBucket(TARGET_RPS)
    session = requests.Session()
    session.headers.update({"User-Agent": HEADERS.get("User-Agent")})

    with open(OUTPUT, "w", newline="", encoding="utf-8") as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["id", "http_status", "error"])
        processed = 0
        futures = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
            for pid in ids:
                futures.append(exe.submit(do_request, session, pid, rate_limiter))
            for fut in as_completed(futures):
                pid, status, err = fut.result()
                writer.writerow([pid, status, err])
                processed += 1
                if processed % 10 == 0 or processed == total:
                    print(f"Progression : {processed}/{total} ({(processed/total)*100:.1f}%)")
    print("✅ Terminé.")

if __name__ == "__main__":
    main()
