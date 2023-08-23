
/*조건에 맞는 도서 리스트 출력하기*/
-- 날짜 데이트 포맷 알아둬야 한다.
-- DATE_FORMAT(날짜 , 형식) : 날짜를 지정한 형식으로 출력
---------- SELECT DATE_FORMAT(NOW(),'%Y-%m-%d') AS 컬럼명 FROM 테이블명
-- YEAR(날짜) : 년도 출력
---------- SELECT YEAR(NOW()) AS 컬럼명 FROM 테이블명

SELECT BOOK_ID, 
DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND YEAR(PUBLISHED_DATE) = 2021 