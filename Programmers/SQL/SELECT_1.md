### 모든 레코드 조회하기

```sql
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

</br>

### 역순 정렬하기

```sql
SELECT NAME, DATETIME FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

</br>

### 아픈 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick';
```

</br>

### 어린 동물 찾기

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION <> 'Aged'
```

</br>

### 동물의 아이디와 이름

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

</br>

### 여러 기준으로 정렬하기

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
```

</br>

### 과일로 만든 아이스크림 고르기

```sql
select A.FLAVOR
from FIRST_HALF A 
left outer join ICECREAM_INFO B on A.FLAVOR = B.FLAVOR
where A.TOTAL_ORDER >3000 AND B.INGREDIENT_TYPE = 'fruit_based'
order by A.TOTAL_ORDER desc
```

</br>

### 12세 이하인 여자 환자 목록 출력하기

```sql
select PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') as TLNO
from PATIENT
where GEND_CD = 'W' and AGE <= 12
order by AGE desc, PT_NAME
```

</br>

### 강원도에 위치한 생산공장 목록 출력하기

```sql
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '%강원도%'
ORDER BY FACTORY_ID ASC
```

</br>

#### 🌱 TIL

- IFNULL과 NVL

  두 함수는 사용 용도는 같으나 사용하는 DBMS에 따라 나뉜다.

  MySQL의 경우에는 IFNULL(VALUE1, VALUE2)

  Oracle의 경우에는 NVL(VALUE1, VALUE2)

  ⇒ value1의 값이 null이면 value2의 값을 출력한다.

</br>