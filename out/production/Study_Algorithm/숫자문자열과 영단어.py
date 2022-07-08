def solution(s):
    answer = 0
    a = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']
    for i in a:
        # s에 있는 i를 숫자(i의 인덱스값)으로 바꿔준다
        # 자리수 고려를 위해서 문자열로 바꿔서 넣어줌
        s = s.replace(i,str(a.index(i)))
    return s

print(solution("one4seveneight"))