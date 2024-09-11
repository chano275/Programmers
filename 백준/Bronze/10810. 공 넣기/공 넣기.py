n, m = map(int, input().split())
li_ijk = [list(map(int, input().split())) for _ in range(m)]

answer = [0 for i in range(n)]

"""
바구니 n개  1 ~ N - 당 공 하나씩 

1 ~ N 번호 공 여러개 
1번 바구니 0개 / 

M번 공 넣기 / 
I ~ J번 바구니에 K번호의 공 넣겠다 
"""

for li in li_ijk:
    for q in range(li[0]-1, li[1]):
            answer[q] = li[2]

for a in answer:print(a, end = ' ')