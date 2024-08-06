T = int(input())


def perm(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i] + arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result


def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result


for tc in range(1, T+1):
    n = int(input())
    n_li = list(range(1, n + 1))  # 1 ~ N 에 대한 리스트
    cooking_table = [list(map(int, input().split())) for _ in range(n)]
    # for i in range(4):
    #     print(cooking_table[i])

    find_min = float('inf')

    # n_li 반 쪼개서 조합 + 뒷부분 찾기
    do_comb = comb(n_li, n / 2)
    do_comb_opposite = []
    compare = []
    for chk in do_comb:  # do_comb : [1, 2, 3, [1, 2, 4] ... / chk : [1, 2, 3]
        # print('##############')
        # print(chk)
        temp = []
        for is_it in n_li: # is_it : 1 ~ n
            if is_it not in chk:
                temp.append(is_it)
        # 해야할 것 같은 가지치기 : # temp 완성 / 이미 나왔던 건지 판단하고 나왔으면 do_comb 에서 빼면서 oppo에 넣지 말아야 하는데...         # if temp not in do_comb:        #     do_comb_opposite.append(temp)
        # chk <> temp 의 순열
        chk_perm, temp_perm = perm(chk, 2), perm(temp, 2)
        c_sum, t_sum = 0,0
        # print(chk_perm, temp_perm)
        for a in chk_perm:c_sum += cooking_table[a[0]-1][a[1]-1]
        for b in temp_perm:t_sum += cooking_table[b[0]-1][b[1]-1]

        find_min = min(find_min, abs(c_sum - t_sum))
        # print(find_min)

    ans = find_min
    print(f'#{tc} {ans}')
    # break