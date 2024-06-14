import sys
from itertools import combinations

def month_to_date(month):
    if month == 1:
        return 0
    elif month == 2:
        return 31
    elif month == 3:
        return 31 + 28
    elif month == 4:
        return 31 + 28 + 31
    elif month == 5:
        return 31 + 28 + 31 + 30
    elif month == 6:
        return 31 + 28 + 31 + 30 + 31
    elif month == 7:
        return 31 + 28 + 31 + 30 + 31 + 30
    elif month == 8:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 9:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 10:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month == 11:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month == 12:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30


nm = sys.stdin.readline()
newNM = nm.split()

N = int(newNM[0])
M = int(newNM[1])
print('N : ', N)
print('M : ', M)

doubleList = []

for i in range(N):
    value = sys.stdin.readline()
    valueList = value.split()

    DD1 = int(valueList[0])
    MM1 = int(valueList[1])
    DD2 = int(valueList[2])
    MM2 = int(valueList[3])
    print(DD1)
    print(MM1)
    print(DD2)
    print(MM2)
    print('i : ', i)
    doubleList.append([])
    doubleList[i].append(month_to_date(MM1) + DD1)
    doubleList[i].append(month_to_date(MM2) + DD2)

    if doubleList[i][1] < doubleList[i][0]:
        doubleList[i].append(doubleList[i][1] - doubleList[i][0] + 365)
    else:
        doubleList[i].append(doubleList[i][1] - doubleList[i][0])

    for j in range(M):
        doubleList[i].append(int(valueList[4 + j]))

print(doubleList)




