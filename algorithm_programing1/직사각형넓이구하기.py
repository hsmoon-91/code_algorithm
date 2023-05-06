# 딕셔너리를 쓰지 않은 경우 
# 키와 값이 있다면 딕션너리 형태로 바꿔서 진행
def solution(dots):
    answer = 0
    if dots[0][0] < 0 :
        x = abs(dots[0][0]) + abs(dots[1][0]) 
    else :
        x = dots[1][0] - dots[0][0]
    if dots[0][1] < 0 :
        y = abs(dots[2][1]) + abs(dots[0][1]) 
    else :
        y = dots[2][1] - dots[0][1]
    answer = x*y
    return answer

def solution(dots): 
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    area = w*h
    return area

def solution(dots): 
    w = max(dots)[0] - min(dots)[0]
    h = max(dots)[1] - min(dots)[1]
    area = w*h
    return area