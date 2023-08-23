/*조건에 맞는 회원수 구하기*/
-- between 함수 사용 방법 알아보기

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 AND AGE >= 20 AND AGE<=29
