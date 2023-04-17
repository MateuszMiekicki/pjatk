import random


def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def lomuto_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)
        lomuto_quicksort(arr, low, pivot_index-1)
        lomuto_quicksort(arr, pivot_index+1, high)


n = 50
arr = [random.randint(0, 99) for i in range(n)]
print("Przed sortowaniem: ", arr)
lomuto_quicksort(arr)
print("Po sortowaniu: ", arr)
