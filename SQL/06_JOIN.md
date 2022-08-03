## 없어진 기록 찾기

- https://programmers.co.kr/learn/courses/30/lessons/59042

~~~sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A RIGHT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID, NAME
~~~

---

## 있었는데요 없었습니다

- https://programmers.co.kr/learn/courses/30/lessons/59043

~~~sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B
ON A

WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
~~~

---

## 오랜 기간 보호한 동물(1)

- https://programmers.co.kr/learn/courses/30/lessons/59044

~~~sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
~~~

---

## 보호소에서 중성화한 동물

- https://school.programmers.co.kr/learn/courses/30/lessons/59045

~~~sql
SELECT A.ANIMAL_ID,	A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE (A.SEX_UPON_INTAKE LIKE 'Intact%') AND (B.SEX_UPON_OUTCOME NOT LIKE 'Intact%')
ORDER BY A.ANIMAL_ID
~~~
