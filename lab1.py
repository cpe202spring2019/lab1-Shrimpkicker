from functools import *
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    max_value = int_list[0]
    for i in range(1,len(int_list)):
        if int_list[i] > max_value:
            max_value = int_list[i] 
    return max_value

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return []
    return reverse_rec(int_list[1:len(int_list)]) + [int_list[0]]

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    
    if int_list == None: #if invalid (None) list is entered, raise an error
        raise ValueError
    if high == low: #When only checking one element of the list, return none if the target isn't at that index
        if int_list[low] == target:
            return low
        else:
            return None
    mid_idx = ((high + low) // 2)
    if int_list[mid_idx] == target:
        return mid_idx
    elif int_list[mid_idx] > target:
        return bin_search(target, low, mid_idx - 1, int_list)
    else:
        return bin_search(target, mid_idx + 1, high, int_list) 
