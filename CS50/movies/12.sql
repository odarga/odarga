SELECT title from movies WHERE id IN
(SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE name = 'Bradley Cooper')
INTERSECT
SELECT title from movies WHERE id IN
(SELECT movie_id FROM stars JOIN people ON stars.person_id = people.id WHERE name = 'Jennifer Lawrence');
