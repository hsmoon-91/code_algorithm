def two_sum(nums, target):
    memo = {} # 딕셔너리 선언
    for v in nums:
        memo[v] = 1
    
    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False

