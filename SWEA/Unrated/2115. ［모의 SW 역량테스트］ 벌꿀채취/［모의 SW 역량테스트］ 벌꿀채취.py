import itertools


# 수 리스트 들어오면 각 리스트 더해서 sum
def cal_square_sum(num_list):
    if sum(num_list) > c: return 0  # 범위 넘으면 컷 (가지치기)
    return sum(num ** 2 for num in num_list)


def cal_max_honey(honey_list):
    max_honey = 0
    for select_cnt in range(1, m + 1):  # 부분집합의 조합을 구한다
        comb = itertools.combinations(honey_list, select_cnt)  # select_cnt 개수만큼의 조합
        comb_list = list(map(cal_square_sum, comb))  # 위의 함수 통해서 연산
        max_honey = max(max_honey, max(comb_list))  # 여태까지 조합 중 가장 이익이 높은 것들로 갱신
    return max_honey


T = int(input())
for tc in range(1, T+1):
    n, m, c = list(map(int, input().split()))    # 벌통 정사각 배열의 가로 / 한마리당 채취 가능 개수 // 채취 가능한 꿀의 최대 양
    honey = [list(map(int, input().split())) for _ in range(n)]

    # 벌 두마리가 가로로 채취 가능 개수를 채우며 최대 양 근접하게 / 최대로 했을 때에 각 칸의 제곱들의 합 중 최대

    max_sum = 0

    for i in range(n):
        for j in range(n-m + 1):
            fst_honey_list = honey[i][j:j+m] # 일꾼 1이 고른 리스트 > 이 list에서 부분집합 구하고, 그중 최대 이익을 구하겠다
            fst_max = cal_max_honey(fst_honey_list)
            for snd_i in range(i, n):
                for snd_j in range(0, n - m + 1):
                    if i == snd_i and snd_j < j + m:continue # 같은 행
                    snd_honey_list = honey[snd_i][snd_j:snd_j + m]  # 일꾼 1이 고른 리스트 > 이 list에서 부분집합 구하고, 그중 최대 이익을 구하겠다
                    snd_max = cal_max_honey(snd_honey_list)

                    max_sum = max(max_sum, fst_max + snd_max)
                    
    print(f'#{tc} {max_sum}')