def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer



def solution(n):
    answer = 0
    num = str(n)
    for i in range(len(num)):
        n = int(num[i])
        answer += n
    return answer