t = int(input())
for test_case in range(1,t+1):
    n = int(input())
 
    a = [list(map(int, input().split())) for  _ in range(n)]
 
    a_    = list(zip(*a))       # 전치행렬
    a_90 = list(zip(*a[::-1])) # 오른쪽 90도
    a_180 = list(zip(*a_90[::-1]))
    a_270 = list(zip(*a))[::-1]  # 270도
 
 
    print(f"#{test_case}")
    for j in range(n):
        _90 = ""
        _180 = ""
        _270 = ""
        for i in range(n):
 
            _90 += str(a_90[j][i])
            _180 += str(a_180[j][i])
            _270 += str(a_270[j][i])
 
        print(_90, _180, _270)