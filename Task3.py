
def min_candy(array):
    length = len(array)
    tempArray = [1] * len(array)

    for i in range(length - 1):
        if array[i + 1] > array[i]:
            tempArray[i + 1] = max(1 + tempArray[i], tempArray[i + 1])

    for i in range(length - 2, -1, -1):
        if array[i] > array[i + 1]:
            tempArray[i] = max(1 + tempArray[i + 1], tempArray[i])
    print(sum(tempArray))
    return sum(tempArray)


arr = [8,4,3,2,1]
arr2 = [3,1,1,3]
arr3 = [7,5,3,1]
arr4 = [1,3,3,3,1]
min_candy(arr)
min_candy(arr2)
min_candy(arr3)
min_candy(arr4)

