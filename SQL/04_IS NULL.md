## 이름이 없는 동물의 아이디

- https://programmers.co.kr/learn/courses/30/lessons/59039

~~~sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL # NULL 값을 가지고 있는 행만 선택
~~~

---

## 이름이 있는 동물의 아이디

- https://programmers.co.kr/learn/courses/30/lessons/59407

~~~sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL # NULL 값이 없는 행만 선택
ORDER BY ANIMAL_ID # ID를 기준으로 오름차순 정렬
~~~

---

## NULL 처리하기

- https://programmers.co.kr/learn/courses/30/lessons/59410
- IFNULL(컬럼명, '대체어')

~~~sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE # NULL값 처리
FROM ANIMAL_INS
ORDER BY ANIMAL_TYPE, NAME, SEX_UPON_INTAKE
~~~

---

