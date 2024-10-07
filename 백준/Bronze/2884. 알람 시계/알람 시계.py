h,m = map(int, input().split())

if h == 0 and m<45:
    h = 23
    m = m + 60-45
    print(h, m)

elif m>=45:
    print(h, m - 45)

elif m<45:
    h -= 1
    m = m + 60 - 45
    print(h, m)