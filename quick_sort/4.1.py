def sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 4, 6]
    arr3 = list(range(1, 101))
    print(arr3)
    print(sum(arr1))
    print(sum(arr2))
    print(sum(arr3))
