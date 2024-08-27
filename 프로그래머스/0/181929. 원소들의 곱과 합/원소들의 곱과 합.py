def solution(num_list):
    gop = 1
    
    for s in num_list:
        gop *= s
    zeg = sum(num_list) ** 2
    
    if gop < zeg: return 1
    else: return 0
    