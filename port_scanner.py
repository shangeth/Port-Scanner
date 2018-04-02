import threading
import socket
from queue import Queue
import time

target = input("Enter the ip to be scanned : ")
no_of_ports = int(input("Enter the number of ports to be scanned(1- ) : "))
t1 = time.time()
print_lock = threading.Lock()




def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port ', port, "is open.")
        con.close()
    except:
        pass


def threader():
    while True:
        scan_port = q.get()
        portscan(scan_port)
        q.task_done()


q = Queue()

for x in range(1000):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for scan_port in range(1, no_of_ports):
    q.put(scan_port)

q.join()
t2 = time.time()
print("Time taken for the scan: ",t2-t1)
