import threading
import time

def fun(seconds):
    print("Sleeping for {} seconds".format(seconds))
    time.sleep(seconds)
    #print("Done sleeping")

time1=time.time()
#normal code
# fun(4)
# fun(3)
# fun(2)

#Threading code
t1=threading.Thread(target=fun,args=[4])
t2=threading.Thread(target=fun,args=[3])
t3=threading.Thread(target=fun,args=[2])
#starting
t1.start()
t2.start()
t3.start()

#joining
t1.join()
t2.join()
t3.join()
#calculating time
time2=time.time()
print(time2-time1)