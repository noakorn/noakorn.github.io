
'''
Computes the number of happy accidents for an input array.
A happy accident is defined as a pair of values (i, j) in the
array where i is positioned to the left of j and i > j.
You may assume all values are distinct.

param:arr: list[int] input array
returns:int: the number of happy accidents
'''


def count_happy_accidents(arr: list) -> int:
    return merge_sort(arr)[1]


def merge_sort(arr, count=0):
    if len(arr) == 1:
        return arr, 0

    middle = len(arr) // 2
    left_sorted_arr, count_from_left = merge_sort(arr[:middle], count)
    right_sorted_arr, count_from_right = merge_sort(arr[middle:], count)
    count += count_from_left + count_from_right
    sorted_arr, count_from_merge = merge(left_sorted_arr, right_sorted_arr)
    count += count_from_merge
    return sorted_arr, count

def merge(left_arr, right_arr):
    count = 0
    sorted_arr = []
    i = 0
    j = 0
    # Once we finished with one of the arrays.
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            count += len(left_arr) - i
            j += 1

    if i < len(left_arr):
        sorted_arr += left_arr[i:]
    else:
        sorted_arr += right_arr[j:]
    return sorted_arr, count
