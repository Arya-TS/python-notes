n = int(input())
l = []

for i in range(n):
    command = input().split()
    operation = command[0]
    args = command[1:]

    if operation == 'insert':
        l.insert(int(args[0]), int(args[1]))

    elif operation == 'print':
        print(l)

    elif operation == 'remove':
        l.remove(int(args[0]))

    elif operation == 'append':
        l.append(int(args[0]))

    elif operation == 'sort':
        l.sort()

    elif operation == 'pop':
        l.pop()

    elif operation == 'reverse':
        l.reverse()
