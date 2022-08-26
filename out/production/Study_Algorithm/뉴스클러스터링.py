from collections import Counter

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i]+str1[i+1])

    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i]+str2[i+1])

    Counter1 = Counter(str1_list)
    Counter2 = Counter(str2_list)

    inter = list((Counter1&Counter2).elements())
    union = list((Counter1|Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter)/len(union) * 65536)
print(solution("FRANCE","french"))