### 상품 별 오프라인 매출 구하기

```mysql
select P.PRODUCT_CODE, sum(P.PRICE * O.SALES_AMOUNT) as SALES
from PRODUCT P
    join OFFLINE_SALE O
    on P.PRODUCT_ID = O.PRODUCT_ID
group by P.PRODUCT_CODE
order by SALES desc, PRODUCT_CODE
```

