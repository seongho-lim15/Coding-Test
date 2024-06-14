import sys

n = int(sys.stdin.readline())
stk = []

for _ in range(n):
    cmdInput = sys.stdin.readline()
    cmdPull = cmdInput.split()
    cmd = cmdPull[0]

    if cmd == 'push':
        stk.append(cmdPull[1])
    elif cmd == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stk))
    elif cmd == 'empty':
        if not stk:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
