/*자동차 대여 기록에서 장기/단기 대여 구분하기*/

-- # 22년 9월 대여기록 대여기간에 대한 컬럼 추가
-- # 띄어쓰기 주의 -> '장기 대여', '단기 대여'
-- # 일수 계산 주의 -> 기간에 대해 +1 을 해주어야 함.
SELECT 
HISTORY_ID, CAR_ID, 
	   DATE_FORMAT (START_DATE, "%Y-%m-%d") AS START_DATE, 
	   DATE_FORMAT (END_DATE, "%Y-%m-%d") AS END_DATE,
       
--  CASE WHEN (END_DATE - START_DATE) + 1 >= 30 THEN '장기 대여' ELSE '단기 대여' END AS RENT_TYPE 
CASE WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여' ELSE '단기 대여' END AS RENT_TYPE 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC