def solution(s1, s2):
    answer = 0
    for val1 in s1 :
        for val2 in s2 :
            if val2 == val1 :
                answer += 1
    return answer