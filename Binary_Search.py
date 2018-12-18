"""Simple binary search function using loops.
Function will take two inputs:
    a Python list to search through, 
    and the value we're searching for.
Assumes the list only has distinct elements, meaning there are no repeated values, 
and elements are in a strictly increasing order.
Returns the index of value, or -1 if the value doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    low = 0 
    high = len(input_array) - 1
    
    
    while (low <= high):
        mid = (low + high)/2
        if (input_array[mid]== value):
            return mid
        elif (input_array[mid]< value):
            low = mid +1 
        else: 
            high = mid - 1 
    
    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)