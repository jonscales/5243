"""
Jon Scales
CMPS 5243  Algorithms & Analysis
Spring 2024
Project 2:  Sort Comparison

Sort Code scripts were modified from those presented by Derrick Sherrill on his youtube channel originally aired 4 years ago.
Merge sort code was modified from FelixTechTips youtube video from 3 years ago.
"""
import random
import timeit
import csv

""" List initializations
    generate a random array based on options
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
              "1":"Bubble Sort",
              "2":"Selection Sort",
              "3":"Insertion Sort",
              "4":"Merge Sort",
              "5":"Quick Sort"
              }
"""
Bubble Sort O(n^2)
"""
def bubbleSort(list):
    list_copy=list[:]
    swapped = True
    n=len(list_copy)-1
    i=0
    while swapped: 
        swapped = False
        for i in range(0,n):
            if list_copy[i]>list_copy[i+1]:
                swapped = True
                list_copy[i],list_copy[i+1] = list_copy[i+1], list_copy[i]                          
    return list_copy   
    

"""
Merge Sort:  O(nlogn)
"""
def mergeSort(list):
    list_copy = list[:]
    if len(list_copy) > 1:
        left = list_copy[:len(list_copy)//2]
        right = list_copy[len(list_copy)//2:]
        print('left array: ' , left)
        print('right array: ' , right)
        mergeSort(left)
        mergeSort(right)


        l = 0 # index positioner for left sublist
        r = 0 # index positioner for right sublist
        m = 0 # index positioner for merged sublists
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list_copy[m] = left[l]
                l+=1
                m+=1 
                               
            else:
                list_copy[m] = right[r]
                r+=1
            
                m+=1 
        print(list_copy)      
        
        while l < len(left):
            list_copy[m] = left[l]
            l+=1
            m+=1
        print(list_copy)
        while r < len(right):
            list_copy[m] = right[r]
            r+=1
            m+=1    
        print(list_copy)
    return list_copy

"""
Selection Sort O(n^2)
"""
def selectionSort(list):
    list_copy=list[:]
    index_length = range(0, len(list_copy)-1)
    for i in index_length:
        min= i
        for j in range(i+1,len(list_copy)):
            if list_copy[j] < list_copy[min]:
                min = j
        if min !=i:
            list_copy[min], list_copy[i] = list_copy[i], list_copy[min]        
    return list_copy
"""
Insertion Sort  O(n^2)
"""
def insertionSort(list):
    list_copy=list[:]
    n=range(1,len(list_copy))
    for i in n:
        value = list_copy[i]
        while list_copy[i-1] > value and i>0:
            list_copy[i], list_copy[i-1] = list_copy[i-1], list_copy[i]
            i-=1            
    return list_copy

"""
Quick Sort O(nlogn)
"""
def quickSort(list):
    list_copy=list[:]
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

if __name__ == "__main__":
    main()



"""



 


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
                print(mergeSort(unsorted_list))
                
            else:
                print("you chose quick sort")
                print(quickSort(unsorted_list))
                
        else:
            print("Invalid option. Please choose from the given options.")
    else:
        print("Invalid option. Please choose from the given options.")
   
   