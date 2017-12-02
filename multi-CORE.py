from multiprocessing import Pool, Process
import time

# # ===================================================
# def sampleProd((num1, num2)):
#     print('num1 * num2 = %r\n' % (num1*num2))
#     return num1*num2

# if __name__=='__main__':
#     sampleProd((4,5))

#     p = Pool(4)
#     p.map(sampleProd, [(1,2), (3,4), (5,6), (7,8)])


# # ==============================
# def f(x):
#     return x*x

# if __name__ == '__main__':
#     p = Pool(5)
#     print(p.map(f, [1, 2, 3]))

# # =============================================
# def worker(num):
#     """thread worker function"""
#     start = time.time()
#     time.sleep(num)
#     print 'Worker:', num, time.time() - start
#     # return

# if __name__ == '__main__':
#     # jobs = []
#     start = time.time()
#     for i in range(5):
#         p = Process(target=worker, args=(i,))
#         # jobs.append(p)
#         p.start()
#     print "finished", time.time()-start



# ==============================================
import multiprocessing
import logging
import sys

def worker():
    print 'Doing some work'
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()