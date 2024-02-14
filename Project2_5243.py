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
              "4":"Merge Sort"
              }
"""
Bubble Sort
"""
def bubbleSort(list):
    swapped = True
    n=len(list)
    i=0
    while swapped: 
        swapped = False
        for i in range(n-1):
            if unsorted_list[i]>unsorted_list[i+1]:
                swap(unsorted_list[i],unsorted_list[i+1])
                swapped = True
                print("made a swap")
        n-=1    
                     
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
    return list

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
            list_type,_ = values
            print(f"{option}: {list_type}")
    
        # Prompt user for sort type input
        sort_choice = input("Enter the number for the type of sort you want to perform: ")
    
        # Check if the user input corresponds to a valid option
        if list_choice in list_options:
            # Get the corresponding list
            selected_list = list_options[list_choice]
            # Call the sort function with the selected list
            if list_choice == 1:
                bubbleSort(unsorted_list)

            elif list_choice == 2:
                selectionSort(unsorted_list)

            elif list_choice == 3:
                insertionSort(unsorted_list)

            else:
                mergeSort(unsorted_list)
        else:
            print("Invalid option. Please choose from the given options.")
    else:
        print("Invalid option. Please choose from the given options.")
   
   