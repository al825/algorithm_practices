"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, debug=False):
    if debug:     
        print ("input array:")
        print(array)
    # input not a list
    if not isinstance(array, list):
        return [array]
    # input is a list of length 1
    elif len(array) == 1:
        return array
    # input is a list of length 20
    elif len(array) == 2:
        return [min(array), max(array)]
    # convention: use the last element as pivot    
    pivot = array[-1]
    pivot_index = len(array) - 1
    i = 0
    while i < pivot_index: 
        if debug:
            print (pivot_index)
            print (array)
        if array[i] > pivot:
            temp_val = array[i]
            array[i] = array[pivot_index-1] # move the element before the pivot to the ith position
            array[pivot_index-1] = pivot # move pivot one step forward
            array[pivot_index] = temp_val # move the ith element after the pivot
            pivot_index -= 1
        else:
            i += 1
    # pivot is the largest in the array
    if pivot_index == len(array)-1:
        return quicksort(array[:pivot_index]) + [pivot]
    # pivot is the smallest in the array
    elif pivot_index == 0:
        return [pivot] + quicksort(array[pivot_index+1:])
    else: 
        return quicksort(array[:pivot_index]) + [pivot] + quicksort(array[pivot_index+1: ])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)


