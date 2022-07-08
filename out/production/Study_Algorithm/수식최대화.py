import itertools
import re

def cal(n1,op,n2):
    if op == "*":
        return n1 * n2
    elif op == "+":
        return n1 + n2
    else:
        return n1 - n2
        
def solution(lines):
    answer = 0
    op_list = list(itertools.permutations(["*","-","+"],3))
    max_num = 0
    for n_op in op_list:
        num =  re.findall(r'\d+', lines)
        ops = re.findall(r'[-*+]', lines)
        for n in n_op:
            while n in ops:
                op = ops.index(n)
                calculate = cal(int(num[op]),n,int(num[op+1]))
                num[op] = calculate
                num.pop(op+1)
                ops.pop(op)

        if max_num < abs(num[0]):
            max_num = abs(num[0])
    
    return max_num

print(solution("100-200*300-500+20"))