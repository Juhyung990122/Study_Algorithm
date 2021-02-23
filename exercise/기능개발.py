def solution(progresses, speeds):
    answer = []
    deploy = list()
    i = 0
    for progress in progresses:
        day = (100-progress) / speeds[i]
        i += 1
        deploy.append(day)
    
    deploy_idx = 0
    for i in range(len(deploy)):
        if deploy[i] > deploy[deploy_idx]:
            answer.append(i-deploy_idx)
            deploy_idx = i
    answer.append(len(deploy)-deploy_idx)
    
    return answer