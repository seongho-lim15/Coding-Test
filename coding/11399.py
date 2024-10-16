N = int(input())

export_times  = list(map(int, input().split(' ')))
export_times.sort()

total_time = 0
acc_time = 0

for idx, export_time in enumerate(export_times):
    acc_time = acc_time + export_time
    total_time = total_time + acc_time


print(total_time)
