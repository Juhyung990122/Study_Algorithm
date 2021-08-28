def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    t = 0
    while bridge:
        #다른 트럭 들어올 공간 마련하고
        bridge.pop(0)
        t += 1
        if truck_weights:
            if sum(bridge)+truck_weights[0] <= weight:
                # 무게검사 통과하면 트럭 넣고
                bridge.append(truck_weights.pop(0))
            # 무게 다 차면 전진시킴
            else:
                bridge.append(0)
        
    return t

print(solution(2,	10,	[7,4,5,6]))