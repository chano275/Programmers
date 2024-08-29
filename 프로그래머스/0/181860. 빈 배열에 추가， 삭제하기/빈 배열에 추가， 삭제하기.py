def solution(arr, flag):
    answer = []
    
    idx = 0
    for tf in flag:
        if tf == True:
            for _ in range(arr[idx] * 2):answer += [arr[idx]]
        else:
            for _ in range(arr[idx]):answer.pop()
            
        idx += 1
    return answer
