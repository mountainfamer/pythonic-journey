from multiprocessing import Process, Pool,Lock
import os, time
lock = Lock()
r = []
def run_proc(name):
    for i in range(5):
        lock.acquire()
        time.sleep(0.2)
        print 'Run child process %s (%s)'% (name, os.getpid())
        lock.release()
    r.append('1')
    print r
    # run_proc('tesst')
if __name__  ==  '__main__':
    # run_proc('test')
    print 'Run the main process (%s). '% (os.getpid())
    mainStart = time.time()
    p = Pool(4)
    print p.__sizeof__()
    for i in range(16):
        p.apply_async(run_proc,args=('Process'+str(i),))
        print p.__sizeof__()
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done'
    mainEnd = time.time()
    print 'All process ran %0.2f seonds.'%(mainEnd-mainStart)