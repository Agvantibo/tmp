query = int(input())
size = int(input())
array = []
for i in range(size):
    array.append([int(i) for i in input().split()])
for i in array:
    flag = False
    for j in i:
        if not flag and j == query:
            flag = True
            print('YES')
    if not flag:
        print('NO')
