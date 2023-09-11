/*진료과별 총 예약 횟수 출력하기*/

-- # 22년 5월에 예약한 환자 수 진료과 코드별
-- # 컬럼명이 STRING 인 경우 ORDER BY 시 컬럼명을 적기 헷갈린다. 이게 맞는지
-- # 컬럼위치를 작성해주면 해결!
SELECT
MCDP_CD AS '진료과코드',
COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY 2, 1