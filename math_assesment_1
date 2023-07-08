def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([10, 14, 3, -1, 7, 15, 8, 25, -6, 9]))

def mergesort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    return merge(mergesort(left), mergesort(right))

print(mergesort([10, 14, 3, -1, 7, 15, 8, 25, -6, 9]))

def selectionsort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

print(selectionsort([10, 14, 3, -1, 7, 15, 8, 25, -6, 9]))

def insertionsort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
                lst[j + 1] = lst[j]
                j -= 1
        lst[j + 1] = key
    return lst

print(insertionsort([10, 14, 3, -1, 7, 15, 8, 25, -6, 9]))

def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubblesort([10, 14, 3, -1, 7, 15, 8, 25, -6, 9]))
