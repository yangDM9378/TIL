CREATE TABLE hotels(
room_num TEXT NOT NULL,
check_in TEXT NOT NULL,
check_out TEXT NOT NULL,
grade TEXT NOT NULL
);


INSERT INTO hotels
VALUES
('B203','2021-12-31','2022-01-03','suite'),
('1102','2022-01-04','2022-01-08','suite'),
('303','2022-01-01','2022-01-03','deluxe'),
('807','2021-01-04','2022-01-07','superior'),
('B205','2022-01-04','2022-01-07','deluxe');

UPDATE hotels
set check_in='2022-01-04'
where room_num='807';

SELECT *
from hotels
where grade='deluxe' or room_num LIKE 'B%';

