"""
Jon Scales
CMPS 5243  Algorithms & Analysis
Spring 2024
Project 2:  Sort Comparison

Code Source & Assistance Reference: 
Bubble, Insertion, Selection & Quick Sort code scripts were modified from 
those presented by Derrick Sherrill on his youtube channel originally aired 4 years ago.
Merge sort code was modified from chat GPT code.
"""
import random
import timeit
import time
import csv

""" List initializations
    generate a random list based on user options
"""
def listInit(size, start_range, end_range): 
    print(f"Random range begins at: ",start_range, " and ends at: ", end_range)
    print(f'The size of the list is ',size, ' elements')
    # generate random values to initialize array
    unsorted_list=[random.randint(start_range, end_range) for _ in range(size)]
    return unsorted_list

def randomize(sorted_list):
    unsorted_list = random.shuffle(sorted_list)
    return unsorted_list
    
""" 
Dictionaries for creating list size and sort type options
for a menu choice user interface
"""    

list_options ={ 
                "0":["TestList",[0,10,100]],
                "1":["1K List",[0,1000,10000]],
                "2":["2K List",[0,1000,10000]],
                "3":["3K List",[0,3000,10000]],
                "4":["4K List",[0,4000,10000]],
                "5":["5K List",[0,5000,10000]],
                "6":["6K List",[0,6000,10000]],
                "7":["7K List",[0,7000,10000]]
            }
sort_options={
              "1":"Bubble Sort - O(n^2)",
              "2":"Selection Sort - O(n^2)",
              "3":"Insertion Sort - O(n^2)",
              "4":"Merge Sort - O(nlogn)",
              "5":"Quick Sort - O(nlogn)"
              }

#Sort methods

"""
Bubble Sort O(n^2)
"""
def bubbleSort(list):
    list_copy=list[:]
    swapped = True
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    n=len(list_copy)-1 # n = length (size) of list - 1 since adding 1 to get last element
    i=0 # index pointer to increment after each loop through list 
    
    #loop until no swaps are made
    while swapped: 
        swapped = False
        #iterate over list checking each pair of adjacent index values for inequality
        for i in range(0,n):
            if list_copy[i]>list_copy[i+1]:
                list_copy[i],list_copy[i+1] = list_copy[i+1], list_copy[i]   # makes a swap
                swapped = True
                ctr +=1
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time, ctr                                   
    
    #return list_copy   
    
"""
Selection Sort O(n^2)
"""
def selectionSort(list):
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    list_copy=list[:]
    index_length = range(0, len(list_copy)-1)
    
    # iterate over list except the last index value & set current index vale to min
    for i in index_length:
        min = i
        #iterate a second time over the list comparing min to adjacent index
        for j in range(i+1,len(list_copy)):
            # reset min to current index if smaller
            if list_copy[j] < list_copy[min]:
                min = j
        # swap current index and original min value if min index has changed
        if min !=i:
            list_copy[min], list_copy[i] = list_copy[i], list_copy[min] # makes a swap
            ctr += 1        
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time, ctr  
    #return list_copy

"""
Insertion Sort  O(n^2)
"""
def insertionSort(list):
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run
    list_copy=list[:]
    n=range(1,len(list_copy)) 
   
    # iterate over list and get index value excepting the 1st index (0) position
    for i in n: 
        value = list_copy[i]
       
        # loop through list comparing value to previous index value 
        while list_copy[i-1] > value and i>0: 
            list_copy[i], list_copy[i-1] = list_copy[i-1], list_copy[i] #swap made
            i-=1
            ctr +=1            
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time, ctr  
    
    #return list_copy

"""
Merge Sort:  O(nlogn)
"""
def mergeSort(list):
    ctr = 0 # counter for swaps
    start_time=time.time() # get start time for run

    list_copy = list[:]

    # check if list has been split into lists of individual elements
    if len(list_copy) > 1:
        # Split the array into two halves
        mid = len(list_copy) // 2
        left = list_copy[:mid]
        right = list_copy[mid:]

        # Recursively sort each half
        ctr_left = mergeSort(left)
        ctr_right = mergeSort(right)
        ctr += ctr_left + ctr_right

        # Merge the sorted halves
        l = r = m = 0  # Index pointers for left list, right list, and merged list respectively
        # loop to compare left & right and add to merged list
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                list_copy[m] = left[l]
                l += 1
            else:
                list[m] = right[r]
                r += 1
            m += 1

        # Copy any remaining elements from left list
        while l < len(left):
            list_copy[m] = left[l]
            l += 1
            m += 1

        # Copy any remaining elements from right list
        while r < len(right):
            list_copy[m] = right[r]
            r += 1
            m += 1
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return execution_time, ctr  
    
    
    return list_copy

"""
Quick Sort O(nlogn)
"""
def quickSort(list):
    list_copy = list[:]
    n=len(list_copy)
    if n<=1:
        return list_copy
    else:
        pivot = list_copy.pop()
        #print("The pivot value is : ", pivot)

    largeList = []
    smallList = [] 

    for item in list_copy:
        if item > pivot:
            largeList.append(item)
        else:
            smallList.append(item)
   
    #sortedList = quickSort(smallList) + [pivot] + quickSort(largeList) 
    
    return quickSort(smallList) + [pivot] + quickSort(largeList)           

"""ChatGPT code for running the analysis using the timeit_timeit module 
import random
import timeit
import csv
"""

# Function to generate a shuffled list of a specified size
def generate_shuffled_list(size):
    lst = list(range(size))
    random.shuffle(lst)
    return lst

# Function to sort a given list (replace this with your sorting function)
def custom_sort(lst):
    return sorted(lst)

# Measure the execution time of the sorting function while ignoring the shuffle function
def measure_sort_execution(size):
    shuffled_list = generate_shuffled_list(size)
    execution_times = []
    for _ in range(10):
        shuffled_list_copy = shuffled_list[:]  # Make a copy to preserve the original shuffled list
        execution_time = timeit.timeit(lambda: custom_sort(shuffled_list_copy), number=1)
        execution_times.append(execution_time)
    average_execution_time = sum(execution_times) / len(execution_times)
    return average_execution_time

# Main function to perform measurements for different list sizes
def main():
    with open('sort_execution_times.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['List Size', 'Average Execution Time (s)'])
        for size in range(1000, 8000, 1000):
            average_execution_time = measure_sort_execution(size)
            csv_writer.writerow([size, average_execution_time])

# if __name__ == "__main__":
#     main()







 


if __name__== "__main__":

    # Display list options to the user
    print("Choose an option for list type:")
    for option, values in list_options.items():
        list_type,_ = values
        print(f"{option}: {list_type}")

    # Prompt user for list size input
    list_choice = input("Enter the number for list size you want to sort: ")

    # Check if the user input corresponds to a valid option
    if list_choice in list_options:
        # Get the corresponding list
        list_type, option_values = list_options[list_choice]
        start_range, size, end_range  = option_values
        
        # call the list initialization function
        
        unsorted_list = listInit(size, start_range, end_range)
        print("The unsorted list is: ", unsorted_list)
        
        # Display sort options to the user
        print("Choose an option for the type of sort to run:")
        for option, values in sort_options.items():
            print(f"{option}: {values}")
    
        # Prompt user for sort type input
        sort_choice = input("Enter the number for the type of sort you want to perform: ")
    
        # Check if the user input corresponds to a valid option
        if sort_choice in sort_options:
            # Call the sort function with the selected list
            if sort_choice == "1":
                print("you chose bubble sort")
                print(bubbleSort(unsorted_list))
               
            elif sort_choice == "2":
                print("you chose selection sort")
                print(selectionSort(unsorted_list))

            elif sort_choice == "3":
                print("you chose insertion sort")
                print(insertionSort(unsorted_list))
               
            elif sort_choice =="4":
                print("you chose merge sort")
                print(merge_sort(unsorted_list))
                
            else:
                print("you chose quick sort")
                print(quickSort(unsorted_list))
                
        else:
            print("Invalid option. Please choose from the given options.")
    else:
        print("Invalid option. Please choose from the given options.")
   
   