SELECT DATE2,CITY,SUM(TOTALPRICE) AS TOTALPRICE
FROM SALES 
WHERE DATE2='2019-01-01'
GROUP BY DATE2,CITY
ORDER BY DATE2,SUM(TOTALPRICE) DESC

--ayn? DATE2 ve CITY de?erlerine sahip sat?rlar bir araya getirilir 
--ve bu gruplar?n toplam fiyatlar? SUM(TOTALPRICE) ile hesaplan?r.

