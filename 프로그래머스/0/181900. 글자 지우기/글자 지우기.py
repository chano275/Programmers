def solution(my_string, indices):
    answer = ''
    li = sorted(indices)
    for i in range(len(my_string)):
        if i in indices:  pass
        else:  answer+=my_string[i]
    return answer