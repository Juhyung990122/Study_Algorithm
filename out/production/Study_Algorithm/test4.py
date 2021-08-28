import sys
from itertools import permutations

# 10넘어가면 약간 힘겨워함.

while True:
    input_data = int(sys.stdin.readline())
    
    if input_data == 0:
        break

    d = list( i for i in range(1,input_data+1))
    for i in list(permutations(d)):
        j = int(''.join(map(str,i)))
        print(j)
    print()


    
