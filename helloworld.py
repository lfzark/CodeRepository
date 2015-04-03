#!/usr/bin/env python
"""
Parallel Hello World
"""

from mpi4py import MPI
import sys
import time

comm=MPI.COMM_WORLD

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank==0:
	data = {'hello,rank one!'}
	comm.send(data,dest=1,tag=22)
	data = {'hello,rank two!'}
	comm.send(data,dest=2,tag=33)

elif rank==1:
	data = comm.recv(source=0,tag=22)
	print data
	sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n"
    % (rank, size, name))
elif rank==2:
	data = comm.recv(source=0,tag=33)
	print data

	sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n"
    % (rank, size, name))
