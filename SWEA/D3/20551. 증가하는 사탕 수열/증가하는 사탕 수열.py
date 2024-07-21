T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    candy = 0

    while a[1] >= a[2]:
        a[1] = a[1] - 1
        candy = candy + 1
    while a[0] >= a[1]:
        a[0] = a[0] - 1
        candy = candy + 1
        
    if a[0] == 0 or a[1] == 0 or a[2] == 0: print(f"#{test_case} -1") 
    else:print(f"#{test_case} {candy}") 