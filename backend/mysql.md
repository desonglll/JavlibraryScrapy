```mysql
SELECT works_table.cast_id                                                     as cast_id,
       TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(cast, ',', n.digit + 1), ',', -1)) AS actor_name
FROM works_table,
     (SELECT 0 digit UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3) n
WHERE LENGTH(cast) - LENGTH(REPLACE(cast, ',', '')) >= n.digit;

```

选择出来所有的cast和cast_id的set

```mysql
SELECT DISTINCT cast_id,
                SUBSTRING_INDEX(cast, ' ', 1) AS actor_name
FROM works_table
WHERE LENGTH(cast) - LENGTH(REPLACE(cast, ' ', '')) = 0;

```