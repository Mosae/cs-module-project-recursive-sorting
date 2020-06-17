# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # BASE CODE
    if end >= start:  # if there is more than 1 element
        mid = (start + end)//2  # find the middle of array.

        if target == arr[mid]:  # if target is in the middle return it
            return mid
        elif arr[mid] > target:  # if target is less than middle we search in lower subarray
            # run the function again 1 position less than target
            return binary_search(arr, target, start, mid - 1)
        else:  # if target is bigger than middle we search in upper subarray + 1
            return binary_search(arr, target, mid + 1, end)
    else:  # else element is not present in array
        return -1

    # if start == end:  # means theres a single element
    #     if(arr[start] == target):  # if the one ele is target then return it else return 0
    #         return start
    #     else:
    #         return -1
    # else:
    #     mid = (start + end)//2  # find the middle of array
    #     if(target == arr[mid]):
    #         return mid
    #     if(target < arr[mid]):
    #         binary_search(arr, target, start, mid - 1)
    #     else:
    #         binary_search(arr, target, mid + 1, end)
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
