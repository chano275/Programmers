def part(arr, idx, cur):
    global max_part

    if idx == m:
       if sum(cur) > c:
           return
       elif cur == []: return
       else:
           cur_s = 0
           for cur_i in cur:
               cur_s += cur_i ** 2
           max_part = max(cur_s, max_part)
           return

    # print(arr, idx, cur)
    part(arr, idx + 1, cur + [arr[idx]])
    part(arr, idx + 1, cur)


def comb(arr, idx, cur):
    global comb_ans

    if len(cur) == 2 or idx == len(arr):
        if len(cur) == 2:
            if cur[0][1] == cur[1][1]:  # 동일한 행
                if cur[0][2] + m - 1 < cur[1][2] or cur[1][2] + m - 1 < cur[0][2]:  # 두 부분집합이 겹치지 않을 때
                    comb_ans.append(cur[0][0] + cur[1][0])
            else:
                comb_ans.append(cur[0][0] + cur[1][0])
        return

    comb(arr, idx + 1,  cur  + [arr[idx]])
    comb(arr, idx + 1,  cur)


T = int(input())
for tc in range(1, T+1):
    n, m, c = list(map(int, input().split()))
    # n : 가로세로
    # m : 벌통의 개수 ( 네모 가로 길이 ) << 2개임
    # c : 한개의 벌통에서 최대로 가능한 값의 합 //

    # 한개의 네모에서 부분집합 > c 넘으면 return 하는 재귀 / 선택 하고 안하고

    honey = [list(map(int, input().split())) for _ in range(n)]

    # n - m + 1 만큼 이동 가능 ( 4 - 2 + 1 >> for문 0 1 2 만큼 시작 좌표 움직이며 )

    ans = []

    # for oneline in honey:
    #     print(oneline)

    for i in range(n):
        for move in range(n-m+1):
            max_part = -float('inf')
            part(honey[i][0 + move : m + move], 0, [])
            ans.append((max_part, i, move)) # i로 세로줄 / move로 0+move ~ m+move-1 까지 idx 일치 확인 가능

    # 겹치면 안되네;
    ans.sort(reverse=True)

    comb_ans = []
    comb(ans, 0, [])
    # print('################################')
    comb_ans.sort(reverse=True)

    # print(comb_ans)

    print(f'#{tc} {comb_ans[0]}')

    # break