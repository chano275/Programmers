t = int(input())
 
for test_case in range(1,t+1):
    n,m = map(int, input().split())
 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    sum = 0
 
    if n<=m:
        diff = m-n
        for i in range(diff + 1): #  이동
            chk = 0
            for j in range(n):chk += a[j] * b[j + i]
            sum = max(sum, chk)
 
    else:
        diff = n-m
        for i in range(diff + 1): #  이동
            chk = 0
            for j in range(m):chk += b[j] * a[j + i]
            sum = max(sum, chk)
 
 
    print(f"#{test_case} {sum}")