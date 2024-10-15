import sys
M = int(sys.stdin.readline())
data_dict = {}

for _ in range(M):
    command = sys.stdin.readline()

    if 'add' in command:
        x = int(command.split(' ')[1])
        data_dict[x] = 1
    elif 'remove' in command:
        x = int(command.split(' ')[1])
        try:
            del data_dict[x]
        except:
            pass
    elif 'check' in command:
        x = int(command.split(' ')[1])
        try:
            if data_dict[x]:
                print(1)
        except:
            print(0)
    elif 'toggle' in command:
        x = int(command.split(' ')[1])
        try:
            del data_dict[x]
        except:
            data_dict[x] = 1
    elif 'all' in command:
        data_dict ={i : 1 for i in range(1, 21)}
    elif 'empty' in command:
        data_dict = {}