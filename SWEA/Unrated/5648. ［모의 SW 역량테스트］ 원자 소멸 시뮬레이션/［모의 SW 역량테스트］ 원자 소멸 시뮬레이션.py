dir_dict = {  # 이동 방향은 상(0), 하(1), 좌(2), 우(3)  /  x y 순이므로 원래와 반대
    0: (0, 0.5),
    1: (0, -0.5),
    2: (-0.5, 0),
    3: (0.5, 0),
}

T = int(input())
for tc in range(1, T+1):
    n = int(input()) # 원자들의 수
    li = [list(map(int, input().split())) for _ in range(n)]
    # 원자 갯수   |   x y dir 에너지(k)

    first_dict = {}
    for _l in li:
        key = (_l[0], _l[1])
        if key in first_dict:
            first_dict[key].append((dir_dict[_l[2]], _l[3]))  # dir & k
        else:first_dict[key] = [(dir_dict[_l[2]], _l[3])]


    # 1,0 : [ ( ( 0, 1 ) , energy )  ]
    ans = 0
    while first_dict:  # 안비어있으면 ㅇㅇ
        # print(first_dict)
        temp_dict = {}
        for k, v in first_dict.items():
            moved_k = (k[0] + v[0][0][0], k[1] + v[0][0][1])

            if moved_k[0] < -1000 or moved_k[0] > 1000 or moved_k[1] < -1000 or moved_k[1] > 1000:continue
            if moved_k in temp_dict:  # 소멸 아녀? > 에너지 더해줘야 하니까 한번 더
                temp_dict[moved_k].append((v[0][0], v[0][1]))
            else:
                temp_dict[moved_k] = [(v[0][0], v[0][1])]

        first_dict = {}
        for k, v in temp_dict.items():
            if len(v) > 1:
                for elem in v:
                    ans += elem[1]
            else:
                first_dict[k] = v

    print(f'#{tc} {ans}')

