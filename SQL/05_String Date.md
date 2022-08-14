## 루시와 엘라 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59046
- WHERE NAME IN('A','B','C') : 특정 컬럼에 표기 되어 있는 것만 호출

~~~sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
# 특정한 이름만 호출
~~~

---

## 이름에 el이 들어가는 동물 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59047

- WHERE 컬럼명 LIKE 문자열

  - ```sql
    WHERE NAME LIKE '%AB%'
    WHERE NAME LIKE 'AB%'
    WHERE NAME LIKE '%AB'
    ```

~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'DOG' #AND 연산으로 정리
ORDER BY NAME
~~~

---

## 중성화 여부 파악하기

- https://programmers.co.kr/learn/courses/30/lessons/59409
- IF문 활용

~~~sql
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%', 'O', 'X') AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
~~~

---

## 오랜 기간 보호한 동물(2)

- https://programmers.co.kr/learn/courses/30/lessons/59411

- DATEDIFF('구분자','Start_Date','End_Date')

  - ```sql
    DATEDIFF(dd,'2018-01-01','2018-12-31') + 1 #365
    #식별자 YY, MM, DD
    ```

~~~sql
SELECT A.ANIMAL_ID, A.NAME # 테이블 표시후 컬럼명
FROM ANIMAL_INS A, ANIMAL_OUTS B # 테이블 2개 불러오기
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(A.DATETIME, B.DATETIME)
LIMIT 2

########################################################################
SELECT B.ANIMAL_ID,	B.NAME, A.DATETIME, B.DATETIME, (A.DATETIME - B.DATETIME) 
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY (B.DATETIME - A.DATETIME) DESC
LIMIT 2
~~~

---

## DATETIME에서 DATE로 형 변환

- https://programmers.co.kr/learn/courses/30/lessons/59414
- DATE_FORMAT ( ) 함수 이용
  - Y : 전체 년도
  - y : 20/19 삭제
  - M : 영어로
  - m : 숫자

~~~sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
~~~

---

