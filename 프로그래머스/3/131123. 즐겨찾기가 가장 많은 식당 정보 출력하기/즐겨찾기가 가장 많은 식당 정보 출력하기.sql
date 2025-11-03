-- 코드를 입력하세요
SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM (
    SELECT 
        FOOD_TYPE,
        REST_ID,
        REST_NAME,
        FAVORITES,
        ROW_NUMBER() OVER (
            PARTITION BY FOOD_TYPE
            ORDER BY FAVORITES DESC
        ) AS rn
    FROM REST_INFO
) f
WHERE rn = 1
ORDER BY FOOD_TYPE DESC;