SELECT DATE2,CITY,SUM(TOTALPRICE) AS TOTALPRICE
FROM SALES 
WHERE DATE2='2019-01-01'
GROUP BY DATE2,CITY
ORDER BY DATE2,SUM(TOTALPRICE) DESC

--aynı DATE2 ve CITY değerlerine sahip satırlar bir araya getirilir 
--ve bu grupların toplam fiyatları SUM(TOTALPRICE) ile hesaplanır.

