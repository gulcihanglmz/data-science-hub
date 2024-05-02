CREATE TABLE PAYMENTS (
ID INT IDENTITY (1,1),
ORDERID INT,
PAYMENTTYPE TINYINT,
DATE_ DATETIME,
ISOK BIT,
APPROVECODE VARCHAR(100),
PAYMENTTOTAL FLOAT,
CONSTRAINT  PK_PAYMENTS PRIMARY KEY CLUSTERED(ID ASC ))
