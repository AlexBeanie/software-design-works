from queue import Queue
import threading
import time

class Services:
    # Queue() is a thread-safe queue implementation
    services = Queue()
    
    def addOrder(self, order):
        self.services.put(order)
        
    def serveOrder(self):
        while True:
            if not self.services.empty():
                order = self.services.get()
                tname = threading.current_thread().name
                print(f"[COCINERO {tname}] Preparando pedido {order[1]} ({order[0]})")
                time.sleep(3)
                print(f"[COCINERO {tname}] Pedido {order[1]} listo: {order[0]} {order[1]} preparada")
            else:
                break
        
    def processOrders(self, numThreads):
        threads = []
        #print(f"Range: {range(0,3)}")
        for i in range(numThreads):
            #print(f"Creating thread {i}")
            threads.append(threading.Thread(target=self.serveOrder, name=i+1))
            threads[i].start()
        
        for thread in threads:
            thread.join()
            
            
        