def recur(n, m):
    if m == 0:
        return 1
    else:
        return n * recur(n, m-1)


for _ in range(10):
    tc = int(input())
    a, b = map(int, input().split())
    c = recur(a, b)
    print(f'#{tc} {c}')
    
