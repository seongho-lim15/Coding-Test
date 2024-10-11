N, K = map(int, input().split(' '))

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i

    # print(result)
    return result


cal_result = factorial(N) // ( factorial(N-K) * factorial(K))
print(cal_result)