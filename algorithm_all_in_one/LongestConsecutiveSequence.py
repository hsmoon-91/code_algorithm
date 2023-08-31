def LongestConsecutiveSewuence(nums):
    
    longest = 0
    num_dict = {}
    
    for num in nums:
        num_dict[num] = True
        
    for num in num_dict:
        if num-1 not in num_dict :
            cnt = 1
            target = num + 1
            while target in num_dict:
                cnt += 1
                target += 1
            longest = max(longest, cnt)
        
    return longest


nums = [6,7,100,5,4,4]

answer = LongestConsecutiveSewuence(nums)
print(answer)