def solution(myString):
    answer = ''
    for s in myString:
        if 'A'<=s<='Z': 
            answer += s 
            continue
        else: 
            answer += chr(ord(s) - 32)
    return answer