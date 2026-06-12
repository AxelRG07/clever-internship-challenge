def integerSort(arr):
    if len(arr) <= 1:
        return arr

    p = arr[len(arr) // 2]

    l = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]

    return integerSort(l) + m + integerSort(r)

inputArr = [5,5,3]

print(integerSort(inputArr))