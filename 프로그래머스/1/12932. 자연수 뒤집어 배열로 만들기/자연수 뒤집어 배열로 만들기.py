def solution(n):
    ans = []
    s = str(n)
    
    for i in range(len(s)):
        ans.append(int(s[len(s) - i - 1]))
    return ans