### 상품 별 오프라인 매출 구하기

```mysql
select P.PRODUCT_CODE, sum(P.PRICE * O.SALES_AMOUNT) as SALES
from PRODUCT P
    join OFFLINE_SALE O
    on P.PRODUCT_ID = O.PRODUCT_ID
group by P.PRODUCT_CODE
order by SALES desc, PRODUCT_CODE
```

</br>

### 조건에 맞는 도서와 저자 리스트 출력하기

```sql
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
FROM BOOK B
    JOIN AUTHOR A
    ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE B.CATEGORY = "경제"
ORDER BY B.PUBLISHED_DATE
```

