def solution(myString):
    ans = myString.split('x')
    print(ans)
    
    ret = []
    
    for s in ans:
        try:
            if 'a' <= s[0] <= 'z': 
                ret.append(s)
        except:
            continue
    
    ret.sort()

    return ret