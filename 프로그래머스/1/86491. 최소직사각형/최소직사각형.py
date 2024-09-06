def solution(sizes):
    answer = 0
    
    g_, s_ = 0, 0
    for s in sizes:
        s = sorted(s)
        
        g_ = max(g_, s[0])
        s_ = max(s_, s[1])
        print(g_, s_)
    
    return g_ * s_