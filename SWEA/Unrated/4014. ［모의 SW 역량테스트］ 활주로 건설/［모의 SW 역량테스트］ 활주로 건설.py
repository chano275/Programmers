# import sys
# sys.stdin = open('sample_input (5).txt')


def flight(arr):
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            cnt += 1
            if cnt > x:  cnt = x

        elif arr[i-1] == arr[i] + 1:  # 하나 감소
            if cnt < 0:  return 0
            cnt = -x + 1  # 체크한 곳부터 x번동안 동일한 원소가 왜야 하므로, -x 에 + 1 해서 카운트에 줌

        elif arr[i-1] == arr[i] - 1:  # 하나 증가
            if cnt == x:
                cnt = 1
            else:
                return 0
        else: return 0

    if cnt >= 0:
        return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    n, x = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(maps[i][j])
        ans += flight(temp)


    # print('########################')

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(maps[j][i])
        ans += flight(temp)


    print(f'#{tc} {ans}')