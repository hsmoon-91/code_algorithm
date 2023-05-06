string = '02984'
# string = '567'


lst = [int(string[x]) for x in range(len(string))]

all = 0 

for i, v in enumerate(lst) :
    if v != 0 :
        if all*v > all+v :
            all *= v
        else :
            all += v
    else :
        all += v

print(all)
        