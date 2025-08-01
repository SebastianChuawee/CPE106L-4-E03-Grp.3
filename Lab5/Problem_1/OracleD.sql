SELECT 
    R.TRIP_DATE AS Class_Date,
    T.TRIP_ID AS Class_Number,
    T.TRIP_NAME AS Class_Description,
    C.CUSTOMER_NUM AS Participant_Number,
    C.LAST_NAME,
    C.FIRST_NAME
FROM 
    TRIP T
JOIN 
    RESERVATION R ON T.TRIP_ID = R.TRIP_ID
JOIN 
    CUSTOMER C ON R.CUSTOMER_NUM = C.CUSTOMER_NUM;
