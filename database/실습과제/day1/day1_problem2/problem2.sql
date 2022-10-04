
CREATE TABLE zoo (
name TEXT NOT NULL,
eat TEXT NOT NULL,
weight INT NOT NULL,
height INT,
age INT
);

INSERT INTO zoo 
VALUES
    ('gorilla', 'omnivore', 215, 180, 5),
    ('rabbit', 'herbivore', 3, 150, NULL),
    ('tiger', 'carnivore', 220, 115, 3),
    ('elephant', 'herbivore', 3800, 280, 10),
    ('dog', 'omnivore', 8, 20, 1),
    ('eagle', 'carnivore', 8, 75, NULL),
    ('dolphin', 'carnivore', 210, NULL, 3),
    ('alligator', 'carnivore', 250, 50, NULL);

SELECT name, height From zoo;

UPDATE zoo
set height=15
where name='rabbit';

select * from zoo where name='rabbit';

select * from zoo where eat ='omnivore';
