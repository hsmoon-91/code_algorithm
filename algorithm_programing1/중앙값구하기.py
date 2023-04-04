def solution(array):
    answer = 0
    array1 = sorted(array)
    idx = round(len(array1) // 2) 
    answer = array1[idx]
    return answer