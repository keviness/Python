from time import *
start = perf_counter()
def gettime():
    s = []
    for i in range(20):
        t = (perf_counter() - start) 
        sleep(0.1)
        s.append(t)
    return s
gettime()
