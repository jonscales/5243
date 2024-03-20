

import random
import timeit
import time
import csv
#from rich import print 
import copy
import sys

"""
Heap sort 
"""
def heapify(list, size, i, ctr=0, execution_time=0):
    start_time=time.time() if execution_time==0 else execution_time  # get start time for run
    largest = i    # Initialize largest as root
    l_child = 2 * i + 1    # left child indexing from 0
    r_child = 2 * i + 2    # right child indexing from 0

    # Check if left child exists and is greater than root
    if l_child < size and list[l_child] > list[largest]:
        largest = l_child

    # Check if right child exists and is greater than the largest so far
    if r_child < size and list[r_child] > list[largest]:
        largest = r_child

    # If the largest is not the root, swap them
    if largest != i:
        list[i], list[largest] = list[largest], list[i]  # swap
        
        # Heapify the root.
        heapify_ctr, heapify_time, list = heapify(list, size, largest, ctr+1, start_time)
    else:
        heapify_ctr = ctr
        heapify_time = time.time() -start_time

    return heapify_ctr, heapify_time, list

def heapSort(heap_list, ctr=0, execution_time=0):
    
    start_time=time.time() if execution_time==0 else execution_time  # get start time for run
    n = len(heap_list)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1,): # range from last element with child to -1 decrementing each time (-1)
        heapify_ctr, heapify_time, heap_list = heapify(heap_list, n, i, ctr+1, start_time)

    # Extract elements one by one
    for i in range(n - 1, 0, -1): # get last element from heap list (last child = n-1) decrement each time (-1)
        heap_list[i], heap_list[0] = heap_list[0], heap_list[i]  # swap
        heapify_ctr, heapify_time, heap_list = heapify(heap_list, i, 0, ctr+1, start_time)
   
    end_time = time.time()
    execution_time = end_time - start_time + heapify_time
    total_ctr = ctr + heapify_ctr
    
    return total_ctr, execution_time, heap_list  



unheaped=[15, 8, 25, 50, 10, 20, 30, 75, 55]
heapSort(unheaped)