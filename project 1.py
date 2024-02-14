

def change(x):
    """ 
    This function used recursion to convert 
    an integer input into its binary equivalent
    and output it as a string to the console.
    """
    if x != 0: # check that the input is >0 
        return str(change(x // 2)) + str(x % 2)
        # x // 2 divides the variable by 2 and returns the integer value without rounding up
        # x % 2 divids the variable by 2 and returns the remainder which is either 1 or 0
        # str converts the int type into a string type and concatenates the modulo portion
        # to a growing string that will represent the binary equivalent of the original variable x
    else:
        return ""


""" loop to check input for valid type and sign"""
while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num<0 :
            raise ValueError("Please enter a positive integer")
        break
    except ValueError as e:
        print(f"Error: {e}. Try again")
              
result = str(change(num))
print(result)