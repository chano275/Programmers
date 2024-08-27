def solution(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    sum1, sum2 = sum(arr1), sum(arr2)
    
    if len1 == len2:
        if sum1 == sum2:
            return 0
        elif sum1 > sum2:
            return 1
        else:
            return -1
    elif len1 > len2:
        return 1
    else:
        return -1
