import sys
stack = list()
answer = list()
possible = True
i = 1

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().rstrip())
    while i <= num:
        stack.append(i)
        answer.append('+')
        i += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        possible = False

if possible == False:
    print("NO")

else:
    print('\n'.join(answer))

