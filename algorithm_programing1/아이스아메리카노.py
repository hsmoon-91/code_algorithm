def solution(money):
    answer = []
    a = money // 5500 
    b = money - (a*5500)
    answer = [a,b]
    return answer