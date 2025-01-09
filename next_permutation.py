# author: Somil chauhan
# date: 09/01/2025
# email: somilkhan755@gmail.com

# Python3 program to find the next Permutation of a given list of numbers

def next_permutation(arr):
    n = len(arr)
    pivot = -1                      # this is for assume the pivot element is -1
    for i in range(n-2, -1, -1):    # this is for loop which iterate from n-2 to 0
        if arr[i] < arr[i+1]:
            pivot = i               # if the element is less than the next element then pivot is equal to i
            break

    if pivot == -1:
        arr.reverse()               # if pivot is -1 means that the array is in descending order so we reverse the array simple
        return arr
    
    for i in range(n-1, pivot, -1):
        if arr[i] > arr[pivot]:      # if the element is greater than the pivot element then swap the element
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    left, right = pivot+1, n-1       # now we reverse the array from pivot+1 to n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Test the function

arr = [1, 2, 3]
print(next_permutation(arr))