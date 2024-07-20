t = int(input())
for test_case in range(1,t+1):
    n,k = map(int, input().split()) # n명중 k번째 학생

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    s = []

    for _ in range(n):
        a,b,c = (map(int, input().split())) # 중간, 기말, 과제
        s.append(a * 0.35 + b * 0.45 + c * 0.2)

    student_k = s[k-1]
    rank = 1

    for i in range(n):
        if student_k == s[i]: pass # 본인
        elif student_k < s[i]:rank += 1

    position = rank * 10 / n # 현재 몇%에 위치하는지 > 30% > 3으로 바꿈 > index 2에 들어가야 함

    # grade의 index : 0~ 10 > 1
                     #~ 100 > 10
    
    for j in range(10):
        if j < position <= j + 1 : # 10까지 가능
            print(f"#{test_case} {grade[j]}")
