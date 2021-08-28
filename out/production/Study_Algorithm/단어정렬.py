import sys
# 다수라인 입력받을땐 이렇게 하기! (시간 거진 9배차이 실ㄹ환가.. )
n = int(sys.stdin.readline())
word_list = set(sys.stdin.readline().rstrip() for i in range(n))

word_list = sorted(word_list)
word_list = sorted(word_list, key = len)
print('\n'.join(word_list))