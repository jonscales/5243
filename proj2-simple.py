


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
Merge sort code was modified from chat GPT code.
"""
import random
import timeit
import time
import csv
#from rich import print 
import copy




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
    
    return ctr, execution_time                                   
    
"""
Selection Sort O(n^2)
"""
def selectionSort(list):
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    n = len(list) - 1
    # print(len(list))
    # print(n)

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
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return ctr, execution_time  

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
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return ctr, execution_time 
    
"""
Merge Sort:  O(nlogn)
"""
def mergeSort(list, ctr=0, execution_time=0):
    #ctr = 0 # counter for swaps
    start_time=time.time() if execution_time == 0 else execution_time  # get start time for run

    # check if list has been split into lists of individual elements
    if len(list) > 1:
        # Split the array into two halves
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Recursively sort each half
        ctr, time_left = mergeSort(left, ctr + 1, start_time)
        ctr, time_right = mergeSort(right, ctr + 1, start_time)
       
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
    
    return ctr, execution_time 

"""
Quick Sort O(nlogn)
"""
def quickSort(list, ctr=0):
    #ctr passed in as default variable set = 0 
    start_time=time.time() # get start time for run
    
    n=len(list)
    if n<=1:
        return ctr, time.time() - start_time
    else:
        pivot = list.pop()
        #print("The pivot value is : ", pivot)

    largeList = []
    smallList = [] 

    for item in list:
        if item > pivot:
            largeList.append(item)
        else:
            smallList.append(item)
    small_ctr, small_time = quickSort(smallList, ctr+1) 
    large_ctr, large_time = quickSort(largeList, ctr+1)
    
    sorted_list = smallList + [pivot] + largeList 
    
    end_time = time.time()
    execution_time = end_time - start_time + small_time + large_time
    total_ctr = ctr + small_ctr + large_ctr
    return total_ctr, execution_time     

""" Shuffle sorted list method"""
def randomize(list):
    random.shuffle(list)
    return list


""" Main portion of program"""
#Loop to make & sort lists
# define list size
#sizes=[1000,2000,3000,4000,5000,6000,7000]
sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
# iterate over sizes list to create lists of random integers for sorting
for size in sizes:
    #iterate over size range to generate 4 randomly filled lists, 1 for each sort type
    unsorted_list=[random.randint(0, 100000) for _ in range(size) ]
    #deep copy unsorted list
    MS = copy.deepcopy(unsorted_list) # merge sort list
    QS = copy.deepcopy(unsorted_list) # quick sort list
    IS = copy.deepcopy(unsorted_list) # insertion sort list
    SS = copy.deepcopy(unsorted_list) # selection sort list
   
   
    #run each sort method on 10 X on its list, randomize list between runs
    for _ in range(10):
       #call sorts on randomized list
        merge_ctr, merge_time = mergeSort(randomize(MS))
        
        with open('merge_sort_data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #write header if file is empty
            if csvfile.tell() == 0:
                csv_writer.writerow(['Sort Type','List Size','Counter #','Execution Time (s)'])
            #write data on subsequent rows    
            csv_writer.writerow(['Merge',size, merge_ctr, merge_time])
              
        quick_ctr, quick_time = quickSort(randomize(QS))

        with open('quick_sort_data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #write header if file is empty
            if csvfile.tell() == 0:
                csv_writer.writerow(['Sort Type','List Size','Counter #','Execution Time (s)'])
            #write data on subsequent rows    
            csv_writer.writerow(['Quick',size, quick_ctr, quick_time])    
        
        insert_ctr, insert_time = insertionSort( randomize(IS))

        with open('insertion_sort_data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #write header if file is empty
            if csvfile.tell() == 0:
                csv_writer.writerow(['Sort Type','List Size','Counter #','Execution Time (s)'])
            #write data on subsequent rows               
            csv_writer.writerow(['Insertion',size, insert_ctr, insert_time])
            

        select_ctr, select_time = selectionSort(randomize(SS))

        with open('selection_sort_data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            #write header if file is empty
            if csvfile.tell() == 0:
                csv_writer.writerow(['Sort Type','List Size','Counter #','Execution Time (s)'])
            #write data on subsequent rows    
            csv_writer.writerow(['Selection',size, select_ctr, select_time])      

