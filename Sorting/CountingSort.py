
def counting_sort(arr):
    # find the maximum of the array
    size = len(arr)
    max_val = int(max(arr))
    min_val = int(min(arr))

    output = [0] * size
    count_arr = [0] * ((max_val - min_val) + 1)

    # note down the position of each element in input array into
    # count array
    for i in range(size):
        count_arr[arr[i] - min_val] += 1

    # cumulative sum of count array
    for j in range(1, len(count_arr)):
        count_arr[j] += count_arr[j-1]

    # formulating the output array
    for k in range(size):
        index = count_arr[arr[k] - min_val] - 1
        output[index] = arr[k]
        count_arr[arr[k] - min_val] -= 1

    return output


if __name__ == '__main__':
    # Test case 1
    input_arr = [4, 2, 2, 8, 3, 3, 1]
    print(counting_sort(input_arr))
    # Test case 2
    input_arr = [-5, -10, 0, -3, 8, 5, -1, 10]
    print(counting_sort(input_arr))