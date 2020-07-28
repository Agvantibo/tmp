def binaryGet(arr, q): 
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
            return 'YES' 
    return 'NO'
input()
array = [int(i) for i in input().split()]
queries = [int(i) for i in input().split()]
for i in queries:
    print(binaryGet(array, i))
