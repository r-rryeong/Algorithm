### 가장 비싼 상품 구하기

```mysql
select max(PRICE) as MAX_PRICE
from PRODUCT
```

</br>

### 가격이 제일 비싼 식품의 정보 출력하기

```mysql
select *
from FOOD_PRODUCT
order by PRICE desc
limit 1
```

</br>

### 최댓값 구하기

```mysql
select DATETIME
from ANIMAL_INS
order by DATETIME desc
limit 1
```

```sql
SELECT MAX(DATETIME)
FROM ANIMAL_INS
```

</br>

### 최솟값 구하기

```mysql
select DATETIME
from ANIMAL_INS
order by DATETIME
limit 1
```

```sql
SELECT MIN(DATETIME)
FROM ANIMAL_INS
```

</br>

### 중복 제거하기

```mysql
select count(distinct name)
from ANIMAL_INS
where name is not null
```

</br>

### 동물 수 구하기

```mysql
select count(*)
from ANIMAL_INS
```

