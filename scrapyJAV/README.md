## Database initialization

修改模型就要修改`.sql`文件和`dbop.mysql_op.init_database()`

```mysql
CREATE TABLE works_table
(
    id            INT AUTO_INCREMENT PRIMARY KEY,
    link          VARCHAR(255),
    preview       VARCHAR(255),
    title         VARCHAR(255),
    serial_number VARCHAR(255),
    release_date  VARCHAR(255),
    length        VARCHAR(255),
    director      VARCHAR(255),
    maker         VARCHAR(255),
    label         VARCHAR(255),
    user_rating   VARCHAR(255),
    genres        VARCHAR(255),
    cast          VARCHAR(255),
    subscribed    VARCHAR(255),
    watched       VARCHAR(255),
    owned         VARCHAR(255)
);
```

```shell
mysql -Dtestsql -u root < database_structure.sql
```

## Export table structure

```shell
mysqldump -u root -p --no-data scrapyjav > database_structure.sql
```