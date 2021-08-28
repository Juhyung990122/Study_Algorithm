def solution(numbers, hand):
    answer = ''
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    keypad = [
        (3,1),(0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)
    ]
    
    l = (3,0)
    r = (3,2)

    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            l = keypad[num]
        elif num in [3,6,9]:
            answer += 'R'
            r = keypad[num]
        else:          
            l_distance = abs(l[0]-keypad[num][0]) + abs(l[1]-keypad[num][1])
            r_distance = abs(r[0]-keypad[num][0]) + abs(r[1]-keypad[num][1]) 
            if l_distance == r_distance:
                if hand == 'right':
                    answer += 'R'
                    r = keypad[num]
                else:
                    answer += 'L'
                    l = keypad[num]
            elif l_distance > r_distance:
                answer += 'R'
                r = keypad[num]
            else:
                answer += 'L'
                l = keypad[num]          
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))