'''from client import *
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

print('Done')'''


from multiprocessing import Process, Pipe

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1
                                              

def event(pid, counter):
    counter += 1
    print('Something happened in {} !'.format(pid) + str(counter))
    return counter

def send_request(pipe1,pipe2, pid, counter,queue):
    #counter += 1
    pipe1.send(('Request', counter,str(pid)))
    pipe2.send(('Request', counter,str(pid)))
    queue.append([counter,str(pid)])
    print('Message sent from ' + str(pid) +' Time :'+ str(counter))
    return counter,queue
    

def recv_request_and_reply(pipe, pid, counter,queue):
    message, timestamp,sender_pid = pipe.recv()
    #counter = calc_recv_timestamp(timestamp, counter)
    queue.append([timestamp,str(sender_pid)])
    print('Message received at ' + str(pid)  +' from ' +str(sender_pid)+' Time :'+  str(counter))
    pipe.send(('Reply', counter,str(pid)))
    return counter,queue

def recv_reply(pipe, pid, counter,reply_count):
    reply_count += 1
    message, timestamp,sender_pid = pipe.recv()
    print('Reply received at ' + str(pid)  +' from ' +str(sender_pid)+' Time :'+  str(counter))
    return counter,reply_count

def process_one(pipe12,pipe13):
    pid = '1'#getpid()
    queue=[]
    counter = 0
    reply_count=0
    counter = event(pid, counter)
    counter,queue = send_request(pipe12,pipe13, pid, counter,queue)
    if(pipe12.poll()):
        counter,queue = recv_request_and_reply(pipe12,pid, counter,queue)
    if(pipe13.poll()):
        counter,queue = recv_request_and_reply(pipe13, pid, counter,queue)
    if(len(queue)==3 and queue[0][1]==str(pid)):
        print("CS Executed by process 1")
    print('queue 1'+repr(queue))

def process_two(pipe21, pipe23):
    pid = '2'#getpid()
    queue=[]
    counter = 0
    counter = event(pid, counter)
    #counter,queue = send_request(pipe12, pid, counter,queue)
    #counter,queue = send_request(pipe13, pid, counter,queue)
    if(pipe21.poll()):
        counter,queue = recv_request_and_reply(pipe21, pid, counter,queue)
    if(pipe23.poll()):
        counter,queue = recv_request_and_reply(pipe23, pid, counter,queue)
    if(len(queue)==3 and queue[0][1]==str(pid)):
        print("CS Executed by process 2")
    print('queue 2'+repr(queue))

def process_three(pipe31, pipe32):
    pid = '3'#getpid()
    queue=[]
    counter = 0
    counter = event(pid, counter)
    #counter,queue = send_request(pipe12, pid, counter,queue)
    #counter,queue = send_request(pipe13, pid, counter,queue)
    if(pipe31.poll()):
        counter,queue = recv_request_and_reply(pipe31, pid, counter,queue)
    if(pipe32.poll()):
        counter,queue = recv_request_and_reply(pipe32, pid, counter,queue)
    if(len(queue)==3 and queue[0][1]==str(pid)):
        print("CS Executed by process 3")
    print('queue 3'+repr(queue))


if __name__ == '__main__':
    pipe12, pipe21 = Pipe()
    pipe23, pipe32 = Pipe()
    pipe13, pipe31 = Pipe()

    process1 = Process(target=process_one,args=(pipe12,pipe13))
    process2 = Process(target=process_two,args=(pipe21,pipe23))
    process3 = Process(target=process_three,args=(pipe31,pipe32))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()