from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print(" rank 0 !") 
    
sum_of_ranks = comm.allreduce(rank, op=MPI.SUM)

print(sum_of_ranks) 
