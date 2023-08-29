def solution(chicken):
    coupon = 0 
    while(coupon == 0) : 
        extra = chicken // 10 
        coupon = chicken % 10
        
        if coupon % 10 == 0:
            extra += 1
        else :
            coupon += coupon
        
    return extra