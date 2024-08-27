n = int(input())
li = list(map(int, input().split()))

ans = float('inf')
ans_list = []

p1 = 0
p2 = len(li) - 1
while 1:
    if p1 == p2:
        break

    # p1 : 앞에서 뒤로 ( -의 수 )
    # p2 : 뒤에서 앞으로 ( +의 수 )

    chk = (li[p1] + li[p2])
    if chk == 0:
        ans_list = [li[p1], li[p2]]
        break

    elif chk > 0:
        temp_ans = ans
        ans = min(ans, abs(chk))
        if temp_ans != ans:
            ans_list = [li[p1], li[p2]]
        p2 -= 1

    else:
        temp_ans = ans
        ans = min(ans, abs(chk))
        if temp_ans != ans:
            ans_list = [li[p1], li[p2]]
        p1 += 1

print(ans_list[0], ans_list[1])