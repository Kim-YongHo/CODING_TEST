## 모든 레코드 조회하기

- https://programmers.co.kr/learn/courses/30/lessons/59034

~~~sql
SELECT  * # (* : 모든 값), (컬러명 : 해당 컬럼만 선택)
FROM ANIMAL_INS # 불러오는 테이블
ORDER BY ANIMAL_ID #오름차순
#ORDER BY ANIMAL_ID DESC #내림차순
~~~

---

## 역순 정렬하기

- https://programmers.co.kr/learn/courses/30/lessons/59035

~~~sql
SELECT NAME, DATETIME # 사용할 컬럼 설정
FROM ANIMAL_INS # 테이블 불러오기
ORDER BY ANIMAL_ID DESC # ANIMAL_ID를 기준으로 역순으로 정렬
~~~

---

## 아픈 동물 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59036

~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick' # WHERE 문법 (문자열은 ''로 표시)
~~~

---

## 어린 동물 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59037

~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged' #어린 동물을 찾기 위해 != 기능을 활용
~~~

---

## 동물의 아이디와 이름

- https://programmers.co.kr/learn/courses/30/lessons/59403

~~~sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID, NAME #기입 순서에 따라 결과에 차이가 있음
~~~

---

## 여러 기준으로 정렬하기

- https://programmers.co.kr/learn/courses/30/lessons/59404
- 다시 풀기

~~~sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC # NAME으로 정렬 그 다음에 DATETIME으로 정렬
#ORDER BY NAME, DATETIME DESC (ASC 생략 가능 기본값 오름차순)
~~~

---

## 상위 n개 레코드

- https://programmers.co.kr/learn/courses/30/lessons/59405

~~~sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1 #1개만 출력해주는 기능 LIMIT
~~~

---

## 모든 레코드 조회하기

- https://programmers.co.kr/learn/courses/30/lessons/59034

~~~sql

~~~

---

## 모든 레코드 조회하기

- https://programmers.co.kr/learn/courses/30/lessons/59034

~~~sql

~~~

---

