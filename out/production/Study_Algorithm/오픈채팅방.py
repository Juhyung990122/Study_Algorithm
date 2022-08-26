def enter(id,name):
    nickname[id] = name
    chat.append(id)
    return nickname,chat
def leave(id):
    chat.pop(chat.index(id))
    return chat
def change(id,name):
    if id in chat:
        nickname[id] = name
    else:
        enter(id,name) 
    return nickname,chat       

def solution(record):
    global answer
    global chat
    global nickname
    answer = list()
    chat = list()
    nickname = dict()

    for i in record:
        info = i.split()
        id = info[1]
        if id not in nickname:
            nickname[id] = ""

        if info[0] == "Enter":
            nickname,chat = enter(info[1],info[2])
        elif info[0] == "Leave":
            chat = leave(info[1])
        elif info[0] == "Change":
            nickname,chat =change(info[1],info[2])

    for i in record:
        info = i.split()
        if info[0] == "Enter":
            answer.append(nickname[info[1]]+"님이 들어왔습니다")
        elif info[0] == "Leave":
            answer.append(nickname[info[1]]+"님이 나갔습니다")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))