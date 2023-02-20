CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
Output will be: 3
Actual Output : 0

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );
Output will be: 2
Actual Output: 2

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );
Output will be : 0
Actual Output: 0

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );
-- Output will be: 2
-- Actual Output: 2