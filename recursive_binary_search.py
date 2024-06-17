"""Recursive Binary Search
The way we've tackled the recursive version of binary search is by using
a combination of a recursive call and the iterative approach
with start and end variables to keep track of the portion of the list we're searching.
"""


def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid - 1)
        else:
            return recursive_binary_search(list, target, mid + 1, end)

def verify(index):
    print("Target found:", result)

numbers = [1, 2, 3,4,5,6,7,8]
result = recursive_binary_search(numbers,12)
verify(result)

result=result= recursive_binary_search(numbers,6)
verify(result)