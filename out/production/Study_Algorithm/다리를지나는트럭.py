def solution(bridge_length, weight, truck_weights):
    answer = 0    
    bridge = [0] * bridge_length
    while True:

        bridge.pop(0)

        if sum(bridge) <= weight and truck_weights:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)

        else:
            bridge.append(0)
        answer += 1

        if sum(bridge) == 0 and len(truck_weights) == 0:
            break

    return answer

print(solution(100,100,[10]))