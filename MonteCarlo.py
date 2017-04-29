import random
import time
from mpi4py import MPI

def comPI(points):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    start = time.time()
    size = comm.Get_size()
    print (comm.Get_rank())
    pi = 0.0
    count = 0.0
    for i in range(points):
        x = random.random()
        y = random.random()
        if(((x*x) + (y*y)) < 1):
            count += 1
    print(time.time() - start)
    pi = (float) (count / points)
    pi = (4.0 / size) * comm.reduce(pi, MPI.SUM )


    return pi


if __name__ == "__main__":
    pi = comPI(100000000)
    comm = MPI.COMM_WORLD
    if comm.Get_rank() == 0:
        print ("Value of PI on ", comm.Get_size(), " processors is ", pi)