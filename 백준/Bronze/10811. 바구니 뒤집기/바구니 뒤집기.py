n, m = map(int, input().split())
li_ijk = [list(map(int, input().split())) for _ in range(m)]

answer = [i for i in range(1, n + 1)]

"""
바구니 n개  1 ~ N - 당 공 하나씩 

1 ~ N 번호 공 여러개 
1번 바구니 0개 / 

M번 공 넣기 / 
I ~ J번 바구니에 K번호의 공 넣겠다 
"""

for li in li_ijk:
    temp_answer = []
    temp_flag = 0
    f, r = li[0] - 1, li[1] - 1
    for i in range(n):
        if f <= i <= r and temp_flag == 0:
            temp_answer += answer[f:r+1][::-1]
            temp_flag = 1
        elif i < f or i > r:
            temp_answer += [answer[i]]

    answer = temp_answer


for a in answer:print(a, end = ' ')