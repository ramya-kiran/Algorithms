

def bubble_sort(arr):
    m = len(arr)

    for i in range(m):
        for j in range(0, m-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    arr = [-10, -20, -30, -40, -50, 5]
    bubble_sort(arr)
    print(arr)