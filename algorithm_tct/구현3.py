n = 'aabbaccc'

for k in range(len(n)) :
    
    nlist = [n[i:i+k] for i in range(0, len(n), k)]