/*없어진 기록 찾기*/

-- 동물 보호소에서 입양을 보낸 기록 : ANIMAL_OUTS 
-- 동물 보호소에 들어온 기록 : ANIMAL_INS 

-- 동물 보호소에서 보냈는데 입양기록이 남지 않은 경우 유실된 ID 찾기
-- 먼저 기준이 되는 테이블에서 유실된 ID를 찾기

SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS AS A LEFT JOIN ANIMAL_INS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL