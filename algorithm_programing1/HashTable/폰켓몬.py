# Level1

def solution(nums):
    # 폰켓몬 전체에서 절반
    choose = int(len(nums)/2)
    
    num = set(nums)
    
    # 중복을 제거한 폰켓몬 수와 전체에서의 절반 중 가장 작은 수를 리턴
    answer = min(len(num),choose)
    
    return answer