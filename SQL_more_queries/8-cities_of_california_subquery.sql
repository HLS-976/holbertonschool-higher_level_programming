-- This script lists all the cities of California that can be found in the database
SELECT id, name FROM cities WHERE state_id = 'California' ORDER BY id;