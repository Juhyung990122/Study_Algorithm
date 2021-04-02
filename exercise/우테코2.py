def solution(word):
    answer = ''
    word_list = ['Z','Y','X','V','U','T','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
    word = list(word)
    for i in word:
        print(i)
        if i == ' ':
            answer += ' '
            continue
        if  65 <= ord(i) <= 90:
            answer += word_list[25-(90-ord(i))-1]
        else:
            answer += word_list[25-(122-ord(i))-1].lower()
    return answer

print(solution('I love you'))