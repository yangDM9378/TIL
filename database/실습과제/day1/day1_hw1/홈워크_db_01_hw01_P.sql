
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
INSERT INTO zoo VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) 고유한 값을 가져야하는 pk인 rowid에 중복된 값을 넣으려 하여 오류가 남
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) NOT NULL 속성이 지정된 weight값을 지정하지 않아 오류발생

INSERT INTO zoo (name, eat, age) VALUES
('dolphin', 'carnivore', 3);