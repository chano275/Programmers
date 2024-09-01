def solution(myStr):
    answer = []
    
    check = ['a', 'b', 'c']
    
    temp = ''
    
    abc_len = 0
    for m in myStr:
        if m not in check:
            temp += m
        else:
            abc_len += 1
            if temp == '':pass
            else: 
                answer.append(temp)
                temp = ''

                
    if temp == '':pass
    else: answer.append(temp)
    
    if abc_len == len(myStr):
        answer.append('EMPTY')
    
    return answer