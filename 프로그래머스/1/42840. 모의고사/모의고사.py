def solution(answers):
    answer = []
    
    s1 = [1,2,3,4,5] * 2000
    s2 = [2,1,2,3,2,4,2,5] * 1250
    s3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    ans = [0,0,0]

    for i in range(len(answers)):
        print(answers[i], s3[i])
        if answers[i] == s1[i]:ans[0]+=1
        if answers[i] == s2[i]:ans[1]+=1
        if answers[i] == s3[i]:ans[2]+=1
            
    for i in range(3):
        if ans[i] == max(ans):
            answer.append(i+1)
        
        
    return answer