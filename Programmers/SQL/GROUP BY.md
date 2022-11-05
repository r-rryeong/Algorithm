### 진료과별 총 예약 횟수 출력하기

```mysql
select MCDP_CD as '진료과 코드', count(APNT_YMD) as '5월예약건수'
from APPOINTMENT
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by count(APNT_YMD), MCDP_CD
```

</br>

### 성분으로 구분한 아이스크림 총 주문량

```mysql
select I.INGREDIENT_TYPE, sum(F.TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF F, ICECREAM_INFO I
where F.FLAVOR = I.FLAVOR
group by I.INGREDIENT_TYPE
order by sum(F.TOTAL_ORDER)
```

</br>

### 동명 동물 수 찾기

```mysql
select NAME, count(NAME) as 'COUNT'
from ANIMAL_INS
where NAME is not null
group by NAME
having count(NAME) >= 2
order by NAME
```

