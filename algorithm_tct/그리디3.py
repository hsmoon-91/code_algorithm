string = '0001100'

min_cnt = len(string)//2
cnt = 0

if string.count('1') <= min_cnt :
    string.replace('1','0')
    cnt += 1

elif string.count('0') <= min_cnt :
    string.replace('0','1')
    cnt += 1

print(cnt)
