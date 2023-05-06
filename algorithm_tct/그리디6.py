# https://school.programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    answer = 0
    sum_sec = 0
    
    while(sum_sec != k) :
        
        for i in range(len(food_times)) :
            
            if food_times[i] > 0 :
                food_times[i] -= 1
                sum_sec += 1
            else : pass
    
    if i == len(food_times)-1 : answer = 1
    else : answer = i+1
        
    return answer