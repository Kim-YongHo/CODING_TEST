## 최댓값 구하기

- https://programmers.co.kr/learn/courses/30/lessons/59415

~~~sql
SELECT MAX(DATETIME) # DATETIME 컬럼에서 MAX값 추출 
FROM ANIMAL_INS # 테이블 불러오기
~~~

---

## 최솟값 구하기

- https://programmers.co.kr/learn/courses/30/lessons/59038

~~~sql
SELECT MIN(DATETIME) # DATETIME 컬럼에서 MIN값 추출 
FROM ANIMAL_INS
~~~

---

## 동물 수 구하기

- https://programmers.co.kr/learn/courses/30/lessons/59406

~~~sql
SELECT COUNT(ANIMAL_TYPE) # COUNT는 NULL값까지 계산
FROM ANIMAL_INS
~~~

---

## 중복 제거하기

- https://programmers.co.kr/learn/courses/30/lessons/59408

~~~sql
SELECT COUNT(DISTINCT NAME) as count # DISTINCT : 중복 제거, 명칭을 count로 변경
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
~~~

---

