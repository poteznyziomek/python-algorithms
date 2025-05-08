class InputError(ValueError): pass


def binary_search(value, a_list, bottom, top):
    '''Return i for which a_list[i] == value, else None.
    
    The input a_list must be sorted in ascending ordrer.
    '''
    if not is_sorted(a_list):
        error_message = \
            'sorted input expected but unsorted given: a_list'
        raise InputError(error_message)
    if bottom > top:
        return None
    middle = (bottom + top) // 2
    if value == a_list[middle]:
        return middle
    elif value < a_list[middle]:
        return binary_search(value, a_list,
            bottom, middle-1)
    else:
        return binary_search(value, a_list, middle+1, top)

def is_sorted(a_list):
    '''Return True if a_list is sorted, False otherwise.'''
    n = len(a_list) - 1
    for i in range(n):
        if a_list[i] > a_list[i+1]:
            return False
    return True