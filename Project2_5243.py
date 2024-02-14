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
def ListInit(choice):
    # start_range = int(input("Enter the start range for a randomly generated set of array values: "))
    # end_range=int(input("Enter the end range for a randomly generated set of array values: "))
    # size = int(input("Enter the number of elements in the array to be randomly generated: "))
   
    option_values = list_options[option]
    start_range, size, end_range  = option_values[1]
    # generate random values to initialize array
    unsorted_list=[random.randint(start_range, end_range) for _ in range(size)]
    return unsorted_list
    
    
    
    


"""  testList """
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
def BubbleSort(list):
    pass


"""
Merge Sort
"""
def MergeSort(list):
    pass

"""
Selection Sort
"""
def SelectionSort(list):
    pass

"""
Insertion Sort
"""
def InsertionSort(list):
    pass

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
        selected_list = list_options[list_choice]
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
                BubbleSort(selected_list)
                
            elif list_choice == 2:
                SelectionSort(selected_list)

            elif list_choice == 3:
                InsertionSort(selected_list)

            elif list_choice == 4:
                MergeSort(selected_list)
            

        else:
            print("Invalid option. Please choose from the given options.")
    else:
        print("Invalid option. Please choose from the given options.")
   
   