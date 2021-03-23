import sys,itertools
operator = ['+','-','*','//']
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
pl,mi,mul,div = list(map(int,sys.stdin.readline().split()))
oper_list = list()
oper_list += ['+'] * pl
oper_list += ['-'] * mi
oper_list += ['*'] * mul
oper_list += ['//'] * div

oper_set = list()
for n in list(itertools.permutations(oper_list,len(oper_list))):
    oper_set.append(n)
oper_set = list(set(oper_set))

max_answer = -1000000001
min_answer = 1000000001
for i in oper_set:
    cal = num[0]
    for j in range(1,len(i)+1):
        if i[j-1]  == '+':
            cal += num[j]
        if i[j-1]  == '-':
            cal -= num[j]
        if i[j-1]  == '*':
            cal *= num[j]
        if i[j-1]  == '//':
            if cal < 0:
                cal = abs(cal) // num[j] * -1
            else:
                cal = cal // num[j]
    if cal < min_answer:
        min_answer = cal
    if cal > max_answer:
        max_answer = cal

print(max_answer)
print(min_answer)     



