import requests
import time
import csv

# === CONFIG ===
INPUT = "post_numbers.txt"
OUTPUT = "addfav_results.csv"
FAILED_OUTPUT = "failed_ids.txt"   # fichier où stocker les IDs en échec

COOKIE_STRING = "gdpr=1; gdpr-consent=1; user_id=5487729; pass_hash=3697e3b5ef16a46ea6acb10b3900e64337f8d60a; comment_threshold=0; post_threshold=0; experiment-mobile-layout=true; cf_clearance=o3xJWzdSVKI9knjFxkkxHSE1z.R0YGay8uQVdDDWGAI-1761005170-1.2.1.1-4cZ82Lfh5Cd6LQ0wAdb63E9rX_2tHDoxE4JxvUToOjVJE2FuEUKLrM_mEy95jNA4gj53dl4MlA3btliGpcwzcQku84JVXeC3TizGvITtr9iK47kSYZiUrdi.M0Kif64bQnIC31BmQSJuPCCnCkqB2z8kmCdwDCFecfld7.aM10a1BvHV8U8AdKScDuzdsJtAqT0IcnVDU4wyu14if928kLq49mCFJUF8i7MYoW6pUvc"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36",
    "Sec-Ch-Ua-Platform": "Linux",
    "Sec-Ch-Ua": '"Not?A_Brand";v="99", "Chromium";v="130"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://rule34.xxx/index.php?page=post&s=view&id=3024475",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": COOKIE_STRING
}

BASE_URL = "https://rule34.xxx/public/addfav.php?id={}"

# === Lecture des IDs ===
with open(INPUT, "r", encoding="utf-8") as f:
    ids = [line.strip() for line in f if line.strip()]

# === Fichiers de sortie ===
session = requests.Session()
session.headers.update({"User-Agent": HEADERS["User-Agent"]})

with open(OUTPUT, "w", newline="", encoding="utf-8") as csvf, \
     open(FAILED_OUTPUT, "w", encoding="utf-8") as failf:
    writer = csv.writer(csvf)
    writer.writerow(["id", "http_status", "error"])

    last_request_time = 0
    total = len(ids)
    for i, pid in enumerate(ids, 1):
        url = BASE_URL.format(pid)

        # Attente pour garantir 1 requête / seconde (min)
        elapsed = time.time() - last_request_time
        if elapsed < 1.0:
            time.sleep(1.0 - elapsed)

        last_request_time = time.time()

        try:
            r = session.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
            status = r.status_code
            if status == 200:
                print(f"✅ ID {pid} ajouté en favori (200)")
                writer.writerow([pid, status, ""])
            else:
                print(f"⚠️ ID {pid} -> HTTP {status}")
                writer.writerow([pid, status, f"HTTP {status}"])
                # écrire l'ID en échec dans le fichier dédié
                failf.write(f"{pid}\n")
                failf.flush()
        except Exception as e:
            print(f"❌ Erreur pour l'ID {pid}: {e}")
            writer.writerow([pid, None, str(e)])
            failf.write(f"{pid}\n")
            failf.flush()

        # Affiche la progression
        if i % 10 == 0 or i == total:
            print(f"Progression: {i}/{total} ({(i/total)*100:.1f}%)")

print("🎯 Terminé.")
