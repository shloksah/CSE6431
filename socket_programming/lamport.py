
from client import *
from server import *
import threading

s1=server()
c1=client()
c2=client()
c3=client()

p1_data=['D 4 A 20','A 57 C 10','C,200 A']
#p2_data=['2 D 4 A 20','4 A 57 C 10','6 C,200 A']
#p1_data=['D 4 A 20','A 57 C 10','C,200 A']
t1 = threading.Thread(target=s1.run, args=())
t2 = threading.Thread(target=c1.run, args=(p1_data,0,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Done')


  
