def solution(a, b):
    s = []
    cnt = 0
    
    if a==b: return a
    elif a < b: 
        while a+cnt != b+1:
            s.append(a+cnt)
            cnt += 1
        return sum(s)
    else:
        while b+cnt != a+1:
            s.append(b+cnt)
            cnt += 1
        return sum(s)