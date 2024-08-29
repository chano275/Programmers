def solution(my_string, s, e):
    answer = ''
    
    target = my_string[s:e+1][::-1]
    print(target)
    
    for i in range(len(my_string)):
        if i < s:
            answer += my_string[i]
        elif s<=i<e+1:
            answer += target[i-s]
        else:answer += my_string[i]
    
    
    return answer