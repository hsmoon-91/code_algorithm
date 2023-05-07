# n = 5
# m = 3
# lst = [1,3,2,3,2]


n = 8
m = 5
# lst = [1,5,4,3,2,4,5,2]
lst = [1,5,4]


all = sum([x for x in range(n)]) # 전체 리스트에서 두개의 쌍에 대한 조합의 합
dup = [x for i, x in enumerate(lst) if i != lst.index(x)] # 리스트에서 같은 값 찾기

print(all-len(dup))


#https://www.techiedelight.com/ko/find-duplicate-items-python-list/

for i, x in enumerate(lst) :
    if i != lst.index(x) :
        print(x)