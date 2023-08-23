/*재구매가 일어난 상품과 회원 리스트 구하기*/
-- 한고객이 여러 상품을 재구매 할 경우도 생각하기 
-- 따라서 group by 할 때 고객 아이디가 아닌 고객 아이디와 제품 아이디로 그룹을 정의한다.


SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) >= 2 
ORDER BY USER_ID, PRODUCT_ID DESC