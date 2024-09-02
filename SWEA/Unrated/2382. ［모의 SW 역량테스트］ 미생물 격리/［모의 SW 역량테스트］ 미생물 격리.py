
dxy = {
    1:(-1,0),
    2:(1,0),
    3:(0,-1),
    4:(0,1)
}


T = int(input())
for tc in range(1, T+1):
    n, m, k = list(map(int, input().split()))
    xy_n_d = [list(map(int ,input().split())) for _ in range(k)]

    first_dict = {}
    for temp in xy_n_d:        first_dict[(temp[0], temp[1])] = [(temp[2], dxy[temp[3]])]  # 미생물 값 / dir

    for _ in range(m):
        # print('##########################')
        # print(first_dict)
        second_dict = {}
        for k, v in first_dict.items():
            nx, ny = k[0] + v[0][1][0], k[1] + v[0][1][1]
            new_key = (nx, ny)

            if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:  # 빨간줄이면 돌리기
                second_dict[new_key] = [(v[0][0] // 2, (-1 * v[0][1][0], -1 * v[0][1][1]))]

            else:
                if new_key in second_dict:                second_dict[new_key].append(v[0])
                else:second_dict[new_key] = v

        first_dict = {}
        # print(second_dict)
        for k, v in second_dict.items():
            if len(v) > 1:
                temp_sum, temp_max, temp_dir = 0, 0, (0, 0)

                for chk in v:
                    temp_sum += chk[0]
                    checker = temp_max
                    temp_max = max(temp_max, chk[0])
                    if checker != temp_max:temp_dir = chk[1]

                first_dict[k] = [(temp_sum, temp_dir)]

            else:first_dict[k] = v

    ans = 0
    for k, v in first_dict.items():
        ans += v[0][0]

    print(f'#{tc} {ans}')

