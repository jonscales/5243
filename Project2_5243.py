"""
Jon Scales
CMPS 5243  Algorithms & Analysis
Spring 2024
Project 2:  Sort Comparison
"""
import random

""" List initializations"""
def ListInit(choice):
    start_range = int(input("Enter the start range for a randomly generated set of array values: "))
    end_range=int(input("Enter the end range for a randomly generated set of array values: "))
    num_values = int(input("Enter the number of elements in the array to be randomly generated: "))
    # generate random values to initialize array
    random_values = [random.randint(start_range, end_range) for _ in range(num_values)]
    unsorted_list=random_values
    return unsorted_list


"""  testList """
list_options ={ 
"1-TestList":[0,10,100],
"2-List1K":[0,1000,10000],
"3-List2K":[0,1000,10000],
"4-List3K":[0,3000,10000],
"5-List4K":[0,4000,10000],
"6-List5K":[0,5000,10000],
"7-List6K":[0,6000,10000],
"8-List7K":[0,7000,10000]
}
list=Print(f'Type in desired List to be sorted: ',)
"""
Bubble Sort
"""
def BubbleSort(list):
    pass


"""
Merge Sort

"""
"""
Selection Sort
"""
"""
Insertion Sort
"""
if __name__== "__main__":


    # Display options to the user
    print("Choose an option:")
    for key in list_options:
        print(f"{key}: {list_options[key]}")

    # Prompt user for input
    user_input = input("Enter the option you want to choose: ")

    # Check if the user input corresponds to a valid option
    if user_input in list_options:
        # Get the corresponding list
        selected_list = list_options[user_input]
        # Call the sort function with the selected list
        sort_list(selected_list)
    else:
        print("Invalid option. Please choose from the given options.")