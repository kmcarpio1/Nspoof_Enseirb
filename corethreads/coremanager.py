import threading
from corethreads.arp import arp
from corethreads.dns_listen import dns_sniffer
from corethreads.arptable import arptable
from corethreads.other_listen import other_sniffer

#
# Handler of the different threads to launch.
#
class ThreadManager:

    def __init__(self):
        self.stopEvent = threading.Event()
        self.startEvent = threading.Event()
        self.thread1 = threading.Thread(target=arp, args=(self.stopEvent,))
        self.thread2 = threading.Thread(target=dns_sniffer, args=(self.stopEvent,))
        self.thread3 = threading.Thread(target=other_sniffer, args=(self.stopEvent,))

    def start_threads(self):
        self.startEvent.set()
        self.thread1.start()
        self.thread2.start()
        self.thread3.start()

manager = ThreadManager()