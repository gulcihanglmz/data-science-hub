CREATE TABLE INVOICEDETAIL(
ID INT IDENTITY (1,1),
INVOICEID INT  ,
ORDERDETAILED INT,
ITEMID INT,
UNITPRICE FLOAT,
LINETOTAL FLOAT
CONSTRAINT  PK_INVOICEDETAIL PRIMARY KEY CLUSTERED([ID] ASC ))