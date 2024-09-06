def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq == '<':
        if eq == '=':
            if n <= m:return 1
            return 0
            
        if n < m:return 1
        return 0
    
    else:
        if eq == '=':
            if n >= m: return 1
            return 0
            
        if n > m: return 1
        return 0
    