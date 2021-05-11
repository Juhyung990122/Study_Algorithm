import sys, math
n = list(map(int,str(sys.stdin.readline().rstrip())))
num_count = [0] * 10

for i in n:
    if i == 6 or i == 9:
        # 한세트에 두번 쓸수있으니까 0.5만 더함
        num_count[6] += 0.5
    else:
        num_count[i] += 1


print(math.ceil(max(num_count)))
