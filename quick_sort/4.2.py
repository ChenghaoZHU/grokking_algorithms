def length(arr):
    if not arr:
        return 0
    else:
        return 1 + length(arr[1:])


if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 = []
    arr3 = [5]
    print(length(arr1))
    print(length(arr2))
    print(length(arr3))
