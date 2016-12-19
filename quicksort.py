"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    print ("input array:")
    print(array)
    if len(array) == 1:
        return array
    pivot = array[-1]
    pivot_index = len(array) - 1
    i = 0
    while i < pivot_index: 
        print (pivot_index)
        print (array)
        if array[i] > pivot:
            temp_val = array[i]
            array[i:pivot_index] = array[i+1: pivot_index+1]
            array[pivot_index] = temp_val
            pivot_index -= 1
        else:
            i += 1
    if pivot_index == len(array)-1:
        quicksort(array[:pivot_index])
        if isinstance(array[:pivot_index]):
            return larray[:pivot_index] + [array[pivot_index]]
        else:
            return [array[:pivot_index]] + [array[pivot_index]]        
    elif pivot_index == 0:
        quicksort(array[pivot_index+1:])
        if isinstance(array[pivot_index+1:], list):
            return array[pivot_index] + [(array[pivot_index+1:])]
        else:
            return list(array[pivot_index]) + list(array[pivot_index+1:
    else: 
        quicksort(array[:pivot_index])
        quicksort(array[pivot_index+1:])
        if isinstance(array[:pivot_index], list):
            if isinstance(array[pivot_index+1:], list):
                return array[:pivot_index] + [array[pivot_index]] + array[pivot_index+1:]
            else:
                return array[:pivot_index] + [array[pivot_index]] + [array[pivot_index+1:]]
        else:
            if isinstance(array[pivot_index+1:], list):
                return [array[:pivot_index]] + [array[pivot_index]] + array[pivot_index+1:]
            else:
                return [array[:pivot_index]] + [array[pivot_index]] + [array[pivot_index+1:]]

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)