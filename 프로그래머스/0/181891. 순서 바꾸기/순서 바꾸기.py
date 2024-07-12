def solution(num_list, n):
    a1 = []
    a2 = []
    
    for i in range(len(num_list)):
        if i < n:             
            a1.append(num_list[i])
        else:                 
            a2.append(num_list[i])
    
    answer = a2 + a1
    
    return answer