import sys

inputValues = sys.stdin.readline().split(' ')
N = int(inputValues[0])
K = int(inputValues[1])
coinValues = []

for i in range(N):
    coinValues.append(int(sys.stdin.readline()))

count = 0
for i in range(N):
    currentCount = K // coinValues[-(i+1)]
    count += currentCount
    K = K % coinValues[-(i+1)]

print(count)