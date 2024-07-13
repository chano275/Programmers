def solution(n):
    s = str(n)
    su = 0
    
    for i in range(len(s)):
        su += int(s[i])
    
    return su