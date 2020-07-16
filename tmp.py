input()
array = [int(i) for i in input().split()]
smallest = array[0]
for i in array:
    if i < smallest:
        smallest = i
array.pop(array.index(smallest))
second_smallest = array[0]
for i in array:
    if i < second_smallest:
        second_smallest = i
print(smallest, second_smallest)
