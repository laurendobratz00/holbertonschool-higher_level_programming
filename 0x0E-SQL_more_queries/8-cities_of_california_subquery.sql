-- a script that lists all the cities of California
-- SELECT
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
