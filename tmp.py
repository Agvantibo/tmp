a = []
stdout = []
while True:
    c = input()
    if c == 'exit':
        stdout.append('bye')
        break
    elif c == 'last':
        stdout.append(a[-1])
    elif c == 'pop':
        stdout.append(a[-1])
        a.pop(-1)
    elif c == 'size':
        stdout.append(len(a))
    elif c == 'clear':
        a = []
        stdout.append('ok')
    elif 'push' in c:
        stdout.append('ok')
        c = c.split()
        a.insert(0, c[1])
print('\n'.join(map(str, stdout)))
