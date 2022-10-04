CREATE TABLE users(
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INT NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INT NOT NULL
);




SELECT COUNT(*) AS '개수' FROM users;

UPDATE users
SET country='경기도'
WHERE first_name='옥자' and last_name='김';

select * from users where first_name='옥자' and last_name='김';

DELETE FROM users where first_name='진호' and last_name='백';

SELECT * FROM users where first_name='진호' and last_name='백';

SELECT country, balance, age from users
where age BETWEEN 30 and 39
group by country;