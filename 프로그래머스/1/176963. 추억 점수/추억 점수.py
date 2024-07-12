def solution(name, yearning, photo):
    answer = []
    
    
    
    for k in photo:
        cnt = 0
        for i in k:
            for chk in range(len(name)):
                if name[chk] == i:
                    cnt += yearning[chk]  
        # 여기서 result 하나 찍어야 함 
        answer.append(cnt)
        
    return answer