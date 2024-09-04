N = int(input())

stack = [int(input()) for _ in range(N)]
flag = False
for i, element in enumerate(stack):
    print(element)

    if element <= N:
        if stack[i] > stack[i+1] and stack[i] != stack[i+1] + 1:
            flag = True
            break

    else:
        if element < stack[i+1]:
            flag = True
            break

print(flag)
