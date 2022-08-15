-- From the two most commonly appearing regions, which is the latest datasource
SELECT DATASOURCE
FROM trips A
    JOIN (
 SELECT REGION, COUNT(0) trips  
    FROM trips
        GROUP BY REGION
        ORDER BY trips DESC
         LIMIT 0,2) B ON (A.REGION = B.REGION)
    ORDER BY DATETIME DESC
    LIMIT 0,1;

-- REGIONS WITH "CHEAP_MOBILE" 
SELECT DISTINCT REGION FROM  trips 
WHERE DATASOURCE = 'CHEAP_MOBILE';