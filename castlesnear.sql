SELECT A.CASTLE_ID,A.NAME CASTLE, A.COUNTRY
FROM CASTLES A, CASTLES B
WHERE A.COUNTRY = B.COUNTRY
AND B.NAME = '&1'
/
SELECT A.CASTLE_ID, A.NAME, B.CASTLE_TYPE_ID, B.TYPE
FROM CASTLES A, CASTLE_TYPES B, CASTLES C
WHERE A.CASTLE_ID = C.CASTLE_ID
AND A.TYPE = B.CASTLE_TYPE_ID
AND C.NAME='&1'
/
