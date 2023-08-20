def solution(N, stages):

    peoples = len(stages)
    users = [ 0 for _ in range(N+1)]
    fails = []
    for stage in stages:
        users[stage-1] +=1
        
    for i in range(N):
        if users[i]==0:
            fails.append([0, i+1])
        else:
            fails.append([users[i]/peoples, i+1])
            peoples-=users[i]
            
    fails.sort(key=lambda x : (-x[0] ))
    answer = []
    for rate, num in fails:
        answer.append(num)
    return answer