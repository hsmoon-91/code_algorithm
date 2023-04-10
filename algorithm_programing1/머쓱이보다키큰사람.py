def solution(array, height):
    array1 = sorted(array)
    answer = 0
    for i in sorted(array) :
        if i > height :
            answer =+ 1
        else : 
            break
    return answer