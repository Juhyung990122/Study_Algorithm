n = int(input())
array = []

for i in range(n):
    info = input().split()
    array.append((info[0],int(info[1])))

array = sorted(array,key = lambda student : student[1])

for i in array:
    print(i[0],end=' ')
