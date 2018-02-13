# [Quick sort]
# Here I present the simple quick sort
# The efficiency can be improved by doing some modification

def quicksort(array):

    if len(array) <= 1:
        return array

    i, pivot = 0, array[0]
    for j in range(len(array))[1:]:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            array[j], array[i+1] = array[i+1], array[j]
            i += 1

    return quicksort(array[:i]) + [pivot] + quicksort(array[i+1:])

# a = [11,2,40,5,21,4,55,7,8,2,9,13]
# b = quicksort(a)
# print(a)
# print(b)
# a.sort()
# print(a == b)

# [Merge sort]

