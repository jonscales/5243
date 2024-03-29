


"""
Jon Scales
CMPS 5243  Algorithms & Analysis
Spring 2024
Project 2:  Sort Comparison

Description
This program will generate data to perform a comparison of 4 sort algorithms: 
merge and quick sort for O(nlogn)-type algorithms and insertion and selection sort for 
O(n^2)-type algorithms.  Each sort method will be run on random lists of integers 
ranging in size from 1000 - 7000 elements. The average execution times and manipulation
counts for 10 consecutive sorts of each list (shuffled between sort operations) will be
calculated and output as data to a .csv file for subsequent graphical analysis.

Code Source & Assistance Reference: 
Bubble, Insertion, Selection & Quick Sort code scripts were modified from 
those presented by Derrick Sherrill on his youtube channel originally aired 4 years ago.
Merge sort code was modified from chat GPT code. Significant question/answer sessions using
ChatGPT were done to learn how to return values as tuples and pass the counter variables 
within the function calls for recursive functions.  My use of ChatGPT is to get python code
syntax as I am still in a learning phase of working with this programming language. 
"""
import random
import timeit
import time
import csv
#from rich import print 
import copy
import sys

#Sort methods
"""
Bubble Sort O(n^2)
"""
def bubbleSort(list):
    swapped = True
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    n=len(list)-1 # n = length (size) of list - 1 since adding 1 to get last element
    i=0 # index pointer to increment after each loop through list 
    
    #loop until no swaps are made
    while swapped: 
        swapped = False
        #iterate over list checking each pair of adjacent index values for inequality
        for i in range(0,n):
            ctr+=1 # list element accessed
            if list[i]>list[i+1]:
                list[i],list[i+1] = list[i+1], list[i]   # makes a swap
                swapped = True
                #ctr +=1 # list elements swapped
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return ctr, execution_time,                                 
    
"""
Selection Sort O(n^2)
"""
def selectionSort(list):
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    n = len(list) - 1

    index_length = range(0, n)
    
    # iterate over list except the last index value & set current index vale to min
    for i in index_length:
        min = i
        ctr+=1 #counter incremented b/c list element accessed
        #iterate a second time over the list comparing min to adjacent index
        for j in range(i+1, len(list)):
            # reset min to current index if smaller
            ctr += 1  # counter incremented b/c list elements accessed 
            if list[j] < list[min]:
                min = j
                
        # swap current index and original min value if min index has changed
        if min !=i:
            list[min], list[i] = list[i], list[min] # makes a swap
            #ctr += 1  # counter incremented b/c list elements swapped       
    select_list = list
    end_time = time.time()
    execution_time = end_time - start_time
    
    return ctr, execution_time, select_list

"""
Insertion Sort  O(n^2)
"""
def insertionSort(list):
    ctr = 0 # counter for element access & swaps
    start_time=time.time() # get start time for run
    n=range(1,len(list)) 
   
    # iterate over list and get index value excepting the 1st index (0) position
    for i in n: 
        value = list[i]
        ctr+=1 # counter incremented b/c list element accessed
       
        # loop through list comparing value to previous index value 
        while list[i-1] > value and i>0: 
            list[i], list[i-1] = list[i-1], list[i] #swap made
            i-=1
            ctr +=1  # counter incremented b/c list elements swapped          
    insert_list = list
    end_time = time.time()
    execution_time = end_time - start_time
    
    return ctr, execution_time, insert_list 
    
"""
Merge Sort:  O(nlogn)
"""
def mergeSort(list, ctr=0, execution_time=0):
    #ctr = 0 # counter for swaps
    start_time=time.time() if execution_time == 0 else execution_time  # get start time for run
    ctr_left=0 if ctr==0 else ctr
    ctr_right=0 if ctr==0 else ctr
    # check if list has been split into lists of individual elements
    if len(list) > 1:
        # Split the array into two halves
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Recursively sort each half
        ctr_left, execution_time, left = mergeSort(left, ctr_left + 1, start_time)
        ctr_right, execution_time, right = mergeSort(right, ctr_right + 1, start_time)
       
        # Merge the sorted halves
        l = r = m = 0  # Index pointers for left list, right list, and merged list respectively
        # loop to compare left & right and add to merged list
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                list[m] = left[l]
                l += 1
            else:
                list[m] = right[r]
                r += 1
            m += 1
            ctr+=1

        # append any remaining elements from left list
        if l < len(left):
            list[m:] = left[l:]
            l += 1
            m += len(left[l:])
            ctr+=1

        elif r < len(right):
            list[m:] = right[r:]
            r += 1
            m += len(right[r:])
            ctr+=1
    
    end_time = time.time()
    execution_time = end_time - start_time
    total_ctr = ctr + max(ctr_left, ctr_right)
    
    return total_ctr, execution_time, list

"""
Quick Sort O(nlogn)
"""
def quickSort(list, ctr=0, execution_time=0): #ctr & time passed in as default variable set = 0 
    start_time=time.time() if execution_time==0 else execution_time  # get start time for run
    quick_list = []
    largeList = []
    smallList = [] 
    
    if len(list) <= 1: # base case when all lists have a single element
        quick_list = list
        return ctr, execution_time, quick_list
    
    # set pivot as value of last element of list
    pivot = list.pop() 
    # print("pivot = [",pivot,"]")
    #compare element values to pivot & assign to sublists
    for item in list:
        if item <= pivot:
            smallList.append(item)
        else:
            largeList.append(item)
    # recursive calls       
    small_ctr, execution_time, small = quickSort(smallList, ctr+1, start_time) 
    large_ctr, execution_time, large = quickSort(largeList, ctr+1, start_time)
    
    quick_list = small + [pivot] + large
   
    end_time = time.time()
    execution_time = end_time - start_time 
    total_ctr = ctr + small_ctr + large_ctr
    
    # print("quick_list: ", quick_list)
    # print("smallList: ", smallList)
    # print("largeList: ", largeList)

    return total_ctr, execution_time, quick_list    

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


"""
Counting sort
"""
def counting_sort(list):
    # Find the maximum value in the array
    max_val = max(list)
    
    # Create a temporaty countint list to store the count of each element
    temp = [0] * (max_val + 1) # makes list with 11 elements all initialized to 0
    
    # Count the occurrences of each element
    # puts the number of times each value occurs in the list into the temp list
    # in the index corresponding to the value of the number (i.e. the number of times
    # 2 appears in the list is stored in temp[2])
    for num in list:
        temp[num] += 1  
    #print("initial temp list:", temp)
    
    # Create the sorted list
    count_list = []
    for i in range(len(temp)):
        count_list.extend([i] * temp[i])
    #print("final temp count array:", temp)
    return count_list

""" 
radix sort
"""
def radixCount(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        radix_list = radixCount(arr, exp)
        exp *= 10
        
    return radix_list

""" Shuffle sorted list method"""
def randomize(list):
    random.shuffle(list)
    return list

""" 
Search Methods
"""
"""
Linear Search
"""
def linearSearch(list,val):
    i = 0
    while i < len(list):
        if list[i] == val:
            return i
        i+=1
    return -1


"""
Binary Search
"""
def binarySearch(list, first, last, val):
    mid = (first + last)//2
    if list[mid] == val:
        return mid
    elif first >= last:
        return -1
    elif val < list[mid]:
        return binarySearch(list, first, mid-1, val)
    else:
        return binarySearch(list, mid+1, last, val)



""" Main portion of program"""
#Loop to make & sort lists
# define list size
#sizes=[1000,2000,3000,4000,5000,6000,7000]
sizes = [20]
max_int = sys.maxsize
merge_ctr_total = merge_time_total=0
quick_ctr_total = quick_time_total=0
insert_ctr_total = insert_time_total=0
select_ctr_total = select_time_total=0
heap_ctr_total = heap_time_total=0

# iterate over sizes list to create lists of random integers for sorting
for size in sizes:
    for j in range(1):
        #iterate over size range to generate 4 randomly filled lists, 1 for each sort type
        #new unsorted list created each sort iteration
        unsorted_list=[random.randint(0 , 100) for s in range(size) ]
        #deep copy unsorted list
        MS = copy.deepcopy(unsorted_list) # merge sort list
        QS = copy.deepcopy(unsorted_list) # quick sort list
        IS = copy.deepcopy(unsorted_list) # insertion sort list
        SS = copy.deepcopy(unsorted_list) # selection sort list
        HS = copy.deepcopy(unsorted_list) # heap sort list
        
        print("iteration ",j+1, unsorted_list)
        # call merge sort
        merge_ctr, merge_time, merge_list = mergeSort(MS)
       
        # calculations        
        merge_ctr_total += merge_ctr
        merge_ctr_avg = merge_ctr_total/10
        merge_time_total += merge_time
        merge_time_avg = merge_time_total/10
        print("iteration ",j+1, merge_list)
        
        # call quick sort      
        quick_ctr, quick_time, quick_list = quickSort(QS)
        # calculations  
        quick_ctr_total += quick_ctr
        quick_ctr_avg = quick_ctr_total/10
        quick_time_total += quick_time
        quick_time_avg = quick_time_total/10
        print("iteration ",j+1, quick_list)

        #call insertion sort 
        insert_ctr, insert_time, insert_list = insertionSort(IS)
        # calculations 
        insert_ctr_total += insert_ctr
        insert_ctr_avg = insert_ctr_total/10
        insert_time_total += insert_time
        insert_time_avg = insert_time_total/10
        print("iteration ",j+1, insert_list)

        # call selection sort 
        select_ctr, select_time, select_list = selectionSort(SS)
        # calculations 
        select_ctr_total += select_ctr
        select_ctr_avg = select_ctr_total/10
        select_time_total += select_time
        select_time_avg = select_time_total/10
        print("iteration ",j+1, select_list)

        # call selection sort 
        heap_ctr, heap_time, heap_list = heapSort(HS)
        # calculations 
        heap_ctr_total += heap_ctr
        heap_ctr_avg = heap_ctr_total/10
        heap_time_total += heap_time
        heap_time_avg = heap_time_total/10
        print("iteration ",j+1, heap_list)

        #reset counter & time variables
        merge_ctr = merge_time=0
        quick_ctr = quick_time=0
        insert_ctr = insert_time = 0
        select_ctr = select_time=0
        heap_ctr = heap_time=0
    
    
    #in 1-10 loop - send avg data to .csv file
    # write data to .csv  
    with open('sort_data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        #write header if file is empty
        if csvfile.tell() == 0:
            csv_writer.writerow(['Sort Type','List Size','Avg Counter','Avg Execution Time (s)'])
        #write data on subsequent rows    
        csv_writer.writerow(['Heap',size, heap_ctr_avg, heap_time_avg])
        csv_writer.writerow(['Merge',size, merge_ctr_avg, merge_time_avg])
        csv_writer.writerow(['Quick', size, quick_ctr_avg, quick_time_avg])   
        csv_writer.writerow(['Insertion',size, insert_ctr_avg, insert_time_avg])
        csv_writer.writerow(['Selection',size, select_ctr_avg, select_time_avg])     
 

