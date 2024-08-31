def solution(arr):
    answer = []
    
    start_idx, end_idx = -1, -1
    
    for i in range(len(arr)):
        if arr[i]==2: 
            start_idx = i
            break
    for i in range(len(arr)):  # -1 = len(arr) - 1  /  -2 = len(arr) - 2
        chk = i + 1  # 1 ~ len(arr)
        
        if arr[-1 * chk] == 2:
            end_idx = -1 * chk + len(arr)
            break
            
    print(start_idx, end_idx)
            
    if start_idx == -1 and end_idx == -1: answer.append(-1)
    elif start_idx == end_idx: answer.append(arr[start_idx])
    else: 
        for i in range(start_idx, end_idx + 1):
            answer.append(arr[i])

        
        
    
    return answer