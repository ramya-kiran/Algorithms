def quick_sort(arr, start, end):

    if start < end:
        partition_index = partition(arr, start, end)
        quick_sort(arr, start, partition_index-1 )
        quick_sort(arr, partition_index+1, end)

    return arr


def partition(arr, start, end):
    pivot = arr[end]
    ptr_i = start - 1

    for ptr_j in range(start, end):

        if arr[ptr_j] < pivot:
            ptr_i += 1
            arr[ptr_i], arr[ptr_j] = arr[ptr_j], arr[ptr_i]

    arr[ptr_i+1], arr[end] = arr[end], arr[ptr_i+1]
    return ptr_i + 1


if __name__ == '__main__':
    input_arr = [10, 80, 30, 90, 40, 50, 70]
    print(quick_sort(input_arr, 0, len(input_arr)-1))
    print(input_arr)