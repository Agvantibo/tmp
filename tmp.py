def binarySearch(arr, q):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < q: 
            low = mid + 1
        elif arr[mid] > q:
            high = mid - 1
        else: 
            return mid
    return -1
input()
array = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]
for i in queries:
    testfield = array.copy()
    rd = binarySearch(array,i)
    print(rd + 1, end=' ')
    testfield.pop(rd)
    while True:
        rd = binarySearch(array,i)
        if rd == -1:
            break
        testfield.pop(rd)
        old = rd
print(old)
