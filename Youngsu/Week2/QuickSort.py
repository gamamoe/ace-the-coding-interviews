import time

import sys
sys.setrecursionlimit(1000000)
print(sys.getrecursionlimit())

arr = list(range(100000))
arr.sort(reverse=True)

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()
print(f"time : {end_time - start_time}")

arr = list(range(100000))
arr.sort(reverse=True)

start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print(f"time : {end_time - start_time}")

arr = list(range(100000))
arr.sort(reverse=True)

start_time = time.time()
arr.sort()
end_time = time.time()
print(f"time : {end_time - start_time}")