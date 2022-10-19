import re 

def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id

    s = re.sub('[^a-z]', '', new_id)

    n = re.sub('[^0-9]', '', new_id)
    if len(n) == 0:
        n = 0
    else: 
        n = int(n)
    n += 1
    return solution(registered_list, s+str(n))
    
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))