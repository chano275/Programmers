n = int(input())  # 약수 갯수
yak = list(map(int, input().split()))

if len(yak) == 1: print(yak[0] ** 2)
elif len(yak) == 2:print(yak[0] * yak[1])
else:
    yak = sorted(yak)
    print(yak[0] * yak[-1])