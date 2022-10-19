from turtle import st


def solution(string):

    if len(string) == 1:
        return list(string)

    front = 1
    back = len(string) - 1
    pre_front = 0
    pre_back = len(string)

    front_answer = list()
    back_answer = list()
    while pre_back > pre_front:
        front_string = string[pre_front:front]
        back_string = string[back:pre_back]

        if(front_string == back_string):
            front_answer.append(front_string)
            back_answer.insert(0, back_string)
            front_string = ""
            back_string = ""
            pre_front = front
            pre_back = back

        front += 1
        back -= 1

    if front_answer == back_answer:
        return front_answer

    return front_answer + back_answer
