import sys

N = int(sys.stdin.readline())
que = []

for i in range(N):
    command = sys.stdin.readline()

    # print(f'{i+1}. before que : {que}')

    if 'push' in command:
        num = int(command.split(' ')[1])
        que.append(num)
    elif 'front' in command:
        try:
            print(que[0])
        except:
            print(-1)
    elif 'back' in command :
        if len(que):
            print(que[-1])
        else:
            print(-1)
    elif 'size' in command :
        print(len(que))
    elif 'empty' in command:
        if len(que)==0:
            print(1)
        else:
            print(0)
    elif 'pop' in command:
        if len(que)>0:
            first_num = que[0]
            print(first_num)
            que = que[1:]
        else:
            print(-1)

    # print(f'{i+1}. after que : {que}')
