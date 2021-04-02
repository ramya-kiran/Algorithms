"""
[1, 6, 1, 2, -1, 4, 5]

l [1, 6, 1] => l [1]  r [6, 1] => [6] [1]

r [2, -1, 4, 5] => [2, -1] [4, 5]

"""


def merge_sort(arr):
    return divide(arr)


def divide(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merge(left, right)


def merge(left_arr, right_arr):
    left_ind, right_ind = len(left_arr), len(right_arr)
    left_ptr, right_ptr = 0, 0
    result = []
    while left_ptr < left_ind and right_ptr < right_ind:
        if left_arr[left_ptr] < right_arr[right_ptr]:
            result.append(left_arr[left_ptr])
            left_ptr += 1
        else:
            result.append(right_arr[right_ptr])
            right_ptr += 1
    if left_ptr < left_ind:
        result.extend(left_arr[left_ptr:])
    else:
        result.extend(right_arr[right_ptr:])
    return result


if __name__ == '__main__':
    # Test case 1
    print(merge_sort([1, 6, 10, 2, -1, 4, 5, -7, 3, 8, 15, 11, 10, -14]))
    # Test case 2
    print(merge_sort([10, 9, 8, 4, 3, 2, 1]))
