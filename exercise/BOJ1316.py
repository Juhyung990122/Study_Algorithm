import sys

n = int(sys.stdin.readline())
answer = 0
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    for i in range(len(string)):
        if i != len(string)-1:
            # 다음글자가 같으면 다음글자로 넘어가기
            if string[i] == string[i+1]:
                pass
            # 다음 글자가 다르면
            else:
                # 그 뒤엔 지금 글자가 나오면 안됨
                # 뒤쪽을 쭉 검사하면서 있으면 이 문자열에 대한 검사 종료
                if string[i] in string[i+1:]:
                    break
        else:
            #끝까지 잘 왔으면
            answer += 1
print(answer)