n = 5
x = [2,3,1,2,2]

new_x = sorted(x, reverse=True)

cnt = 0 # 그룹의 개수
all_sum = 0 # 전체 사람수
remain = n

while(n > all_sum) :
    
    remain = remain % max(new_x)
    all_sum += max(new_x)
    cnt += 1
    del new_x[:(max(new_x))]
        
print(cnt)
