def solution(myString, pat):
    answer = 0
    
    # pat - 
    
    for i in range(len(myString)):
        if i >= len(pat) - 1: # 2 < 012 
            target = myString[i - (len(pat) - 1) : i+1]  # 0 ~ 2
            if target == pat:
                answer += 1
    
    return answer