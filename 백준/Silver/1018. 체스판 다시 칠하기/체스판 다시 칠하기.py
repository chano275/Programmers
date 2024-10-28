m, n = map(int, input().split())
maps = [list(map(str, input())) for _ in range(m)]


ans = float('inf')

for _i in range(m-8 + 1):  # + 1 ?
    for _j in range(n-8 + 1):
        ans1, ans2 = 0, 0
        p2_white, p2_black = 0, 0
        p1_white, p1_black = 0, 0

        for i in range(8):
            for j in range(8):
                if ((_i + i) + (_j + j)) % 2 == 0:  # 더해서 짝수 다 w 로 가정
                    if maps[_i + i][_j + j] == 'W':p2_white += 1  # 짝수 하양
                    else:p2_black += 1                  # 짝수 검정
                else:
                    if maps[_i + i][_j + j] == 'W':p1_white += 1  # 홀수 하양
                    else:p1_black += 1                  # 홀수 검정

        # 짝수 검정, 홀수 하양
        ans1 = ans1 + p2_white + p1_black

        # 짝수 하양, 홀수 검정
        ans2 = ans2 + p2_black + p1_white

        ans = min(ans, ans1, ans2)

print(ans)