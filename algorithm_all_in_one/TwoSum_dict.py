# hash table / dictionary / array list based

def two_sum(nums, target):
    memo = {} # 딕셔너리 선언
    
    for v in nums: # 리스트 값을 딕셔너리에 채운다.
        memo[v] = True 
    
    for v in nums:
        needed_number = target - v
        if needed_number in memo and needed_number != v: # 딕셔너리에서 값을 찾는다.
            return True
    return False

# value = two_sum(nums=[4,1,9,7,5,3,16], target=14)
value = two_sum(nums=[4,1,9,7,11], target=14)
print(value)
