import math
def solution(n, words):
    answer = [0,0]
    who = 1
    for i in range(1,len(words)):
        who = who % n
        #끝글자랑 안맞을때 + 중복
        if words[i-1][-1] != words[i][0] or (words[i] in words[0:i]):
            answer = [who+1,i//n+1]
            return answer
        who += 1
    return answer 
        

#print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(3,"tank", "kick", "know", "wheel", "land", "dream", "mrobot","test", "tank"]))
