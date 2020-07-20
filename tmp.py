query = int(input())
size = int(input())
array = []
for i in range(size):
    array.append([int(i) for i in input().split()])
for i in range(size):
    flag = False
    for j in range(size):
        if not flag and array[j][i] == query:
            flag = True
            print('YES')
    if not flag:
        print('NO')
