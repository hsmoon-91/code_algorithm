n = 5
lst = [3,2,1,1,9]

# n = 3
# lst = [3,5,7]


val = 0
loop_val = 0

while(loop_val >= 0) :
    
    val += 1
    loop_val = val
    for i, v in enumerate(lst) :
        if loop_val not in lst :
            loop_val = loop_val-v
            lst.remove(v)
        else : break
    
print(val)