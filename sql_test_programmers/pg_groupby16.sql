/*식품분류별 가장 비싼 식품의 정보 조회하기*/
-- # 식품분류별로 가격이 제일 비싼 식품의 분류 가격 이름
-- # 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- # 서브쿼리를 이용하여야 하는가...
SELECT
CATEGORY, 
PRICE,
PRODUCT_NAME
FROM
FOOD_PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
GROUP BY CATEGORY
HAVING CATEGORY IN ('과자','국','김치','식용유')
ORDER BY PRICE DESC