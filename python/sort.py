# [Quicksort]
# Here I present the simple quick sort
# The efficiency can be improved by doing some modification

def quicksort(array):
    if len(array) <= 1:
        return array

    i, pivot = 0, array[0]
    for j in range(len(array))[1:]:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            array[j], array[i + 1] = array[i + 1], array[j]
            i += 1

    return quicksort(array[:i]) + [pivot] + quicksort(array[i + 1:])

# [Quicksort] - modified
# We can modify the quicksort which considers the case pivot == array[k] as well
# The performance is much better than simple quicksort if there is duplicate elements in the list

def quick_sort(array):
    if len(array) <= 1:
        return array

    i, j, pivot = 0, 0, array[0]
    for k in range(len(array))[1:]:
        if array[k] < pivot:
            array[i], array[k] = array[k], array[i]
            array[k], array[j + 1] = array[j + 1], array[k]
            i += 1
            j += 1
        elif array[k] == pivot:
            array[k], array[j + 1] = array[j + 1], array[k]
            j += 1

    return quick_sort(array[:i]) + [pivot] * (j - i + 1) + quick_sort(array[j + 1:])

# ---------------------------------------------------------------------------------------------------
#
# from random import randint
#
# a = []
# for i in range(10000):
#     a.append(randint(0, 1000))
#
# b = quicksort(a)
# a.sort()
# print(a == b)
#
# ---------------------------------------------------------------------------------------------------

#  [Merge sort]

def merge_sort(array):

    length = len(array)
    if length <= 1:
        return array

    mid = int((length-1)/2)
    left = merge_sort(array[:mid+1])
    right = merge_sort(array[mid+1:])

    i = j = 0
    new_array = []
    while i < (mid+1) and j < length-(mid+1):
        if left[i] < right[j]:
            new_array.append(left[i])
            i += 1
        else:
            new_array.append(right[j])
            j += 1
    new_array += left[i:] + right[j:]

    return new_array

# ---------------------------------------------------------------------------------------------------
#
# from random import randint
#
# a = []
# for i in range(10000):
#     a.append(randint(0, 1000))
#
# b = merge_sort(a)
# a.sort()
# print(a == b)
#
# ---------------------------------------------------------------------------------------------------

# [Insertion sort]
# Time complexity is O(N^2) (best case: O(N)). Not efficient.

def insertion_sort(array):

    for i in range(len(array))[1:]:
        cur = array[i]
        j = i-1
        while j >= 0 and array[j] > cur:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = cur

    return array

# ---------------------------------------------------------------------------------------------------
#
# from random import randint
#
# a = []
# for i in range(10000):
#     a.append(randint(0, 1000))
#
# b = insertion_sort(a)
# a.sort()
# print(a == b)
#
# ---------------------------------------------------------------------------------------------------