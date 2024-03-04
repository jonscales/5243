def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_val + 1) # makes list with 11 elements all initialized to 0
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    print(count)
    # Create the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Example usage:
arr = [3,10, 2, 3, 1, 0, 4, 8, 2, 1]
sorted_arr = counting_sort(arr)
print("Original array:", arr)

print("Sorted array:", sorted_arr)
