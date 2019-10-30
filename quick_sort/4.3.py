def max(arr):
    if len(arr) == 1:
        return arr[0]

    candidate = max(arr[1:])
    if arr[0] >= candidate:
        return arr[0]
    else:
        return candidate


if __name__ == '__main__':
    arr1 = [1, 3, 5]
    arr2 = [19, 3, 24, 11]
    arr3 = [5]
    print(max(arr1))
    print(max(arr2))
    print(max(arr3))
