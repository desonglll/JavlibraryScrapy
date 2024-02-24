## Database initialization

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