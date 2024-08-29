def solution(intStrs, k, s, l):
    answer = []
    
    temp = []
    for i in intStrs:
        temp.append(int(i[s:s+l]))
        
    for t in temp:
        if t > k:
            answer.append(t)
        
    
    return answer