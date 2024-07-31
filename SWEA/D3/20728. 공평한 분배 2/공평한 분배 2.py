def comb(arr, n):
    global min_mm_diff

    for i in range(len(arr) - n + 1):
        check_arr = arr[i   :  n + i]
        if min_mm_diff > (check_arr[-1] - check_arr[0]):
            min_mm_diff = (check_arr[-1] - check_arr[0])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split())) # 사탕의 개수  /  len = N
    min_mm_diff = 10 ** 9 + 1

    candy.sort()
    comb(candy, K)

    print(f'#{tc} {min_mm_diff}')