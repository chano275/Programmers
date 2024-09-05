import heapq


def check(li):
    for l in li:
        if -l >= h:
            return 0
    return 1


n, h, t = list(map(int, input().split()))  # 인구 / 센티 키 / 뿅망치 횟수
arr = [-1 * int(input()) for _ in range(n)]
heapq.heapify(arr)

if h == 1 and h == -1 * arr[0]:    print('NO\n1')
else:
    flag = 0
    t_cnt = 0
    for _ in range(t):
        if check(arr) == 1:
            print(f'YES\n{t_cnt}')
            flag = 1
            break # 조건 만족하면 1 / 아니면 0
        max_v = -heapq.heappop(arr)
        heapq.heappush(arr, -(max_v // 2))
        t_cnt += 1

        if check(arr) == 1:
            print(f'YES\n{t_cnt}')
            flag = 1
            break # 조건 만족하면 1 / 아니면 0

    if flag == 0:
        print(f'NO\n{-min(arr)}')
