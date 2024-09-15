n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())


ans = 0
for i in range(n):
    ans += 1
    target = people[i] - b

    if target < 0:continue

    if target % c == 0:
        ans += (target // c)
    else:
        ans += ((target // c) + 1)

print(ans)