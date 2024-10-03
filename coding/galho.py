n = int(input())
stk = []
is_success = True
result_stk = []
for _ in range(n):
    input_str=input()
    stk=[]
    is_success = True
    # print(f'input_str : {input_str}')
    for char in input_str:
        # print(f'char : {char}')

        if char == '(':
            stk.append('(')
        elif len(stk)>0 and char== ')':
            stk.pop()
        else:
            # print('Fail : To many ) ')
            is_success=False

    if len(stk)>0:
        # print('Fail : To Long ')
        is_success = False

    if is_success :
        # print('YES')
        result_stk.append('YES')
    else:
        # print('NO')
        result_stk.append('NO')

for result in result_stk:
    print(result)
