"""
Jon Scales
CMPS 5243  Algorithms & Analysis
Spring 2024
Project 2:  Sort Comparison
"""
import random

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

def swap(x,y):
    return y, x
    
    

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
Bubble Sort
"""
def bubbleSort(list):
    swapped = True
    n=len(list)-1
    i=0
    while swapped: 
        swapped = False
        for i in range(0,n):
            if unsorted_list[i]>unsorted_list[i+1]:
                swapped = True
                unsorted_list[i],unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                print("made a swap")
                          
    return list    
    

"""
Merge Sort
"""
def mergeSort(list):


    return list

"""
Selection Sort
"""
def selectionSort(list):
    return list
"""
Insertion Sort
"""
def insertionSort(list):
    n=range(1,len(list))
    for i in n:
        value = list[i]
        while list[i-1] > value and i>0:
            list[i], list[i-1] = list[i-1], list[i]
            i-=1
            
    return list

"""
Quick Sort
"""
def quickSort(list):
    n=len(list)
    sortedList=[]
    if n<=1:
        return list
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
   
    #sortedList = quickSort(smallList) + [pivot] + quickSort(largeList) 
    
    return quickSort(smallList) + [pivot] + quickSort(largeList)           

 


 


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
                selectionSort(unsorted_list)

            elif sort_choice == "3":
                print(insertionSort(unsorted_list))
               
            elif sort_choice =="4":
                print(mergeSort(unsorted_list))
                

            else:
                print(quickSort(unsorted_list))
                
        else:
            print("Invalid option. Please choose from the given options.")
    else:
        print("Invalid option. Please choose from the given options.")
   
   