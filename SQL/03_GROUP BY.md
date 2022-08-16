## 고양이와 개는 몇 마리 있을까

- https://programmers.co.kr/learn/courses/30/lessons/59040

~~~sql
SELECT ANIMAL_TYPE, COUNT(*) AS count #COUNT(*) 모든것 카운트
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE # 동물형태로 그룹화
ORDER BY ANIMAL_TYPE # 동물형태로 정렬
~~~

---

## 동명 동물 수 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59041

~~~sql
SELECT NAME, COUNT(NAME) AS COUNT # COUNT(*) = COUNT(NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT > 1 #SELECT 부분에 선언한 명칭을 기입해야 동작
ORDER BY NAME



SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS 
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME;

~~~

---

## 입양 시각 구하기(1)

- https://programmers.co.kr/learn/courses/30/lessons/59412

- 날짜 추출

  - ```SQL
    SELECT YEAR(DATETIME)
    SELECT MONTH(DATETIME)
    SELECT DAY(DATETIME)
    SELECT HOUR(DATETIME)
    SELECT MINUTE(DATETIME)
    SELECT SECOND(DATETIME)
    ```

  - ```sql
    # 특정 구간 출력
    SELECT HOUR(DATETIME)
    HAVING HOUR BETWEEN 0 AND 19
    ```

~~~sql
SELECT HOUR(DATETIME), COUNT(*) AS COUNT # 모든 값을 카운트
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20 # 9~20 까지 선택
GROUP BY HOUR(DATETIME) # 그룹화
ORDER BY HOUR(DATETIME) # 정렬



SELECT HOUR(DATETIME) AS 'HOUR', COUNT(DATETIME) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY HOUR(DATETIME)
ORDER BY HOUR
~~~

---

## 입양 시각 구하기(2)

- https://programmers.co.kr/learn/courses/30/lessons/59413
- SET @HOUR 에 대한 학습 필요

~~~sql
SET @HOUR := -1;
SELECT (@HOUR := @HOUR+1) AS 'HOUR',
       (SELECT COUNT(*) 
        FROM ANIMAL_OUTS 
        WHERE HOUR(DATETIME) = @HOUR) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
~~~

---
