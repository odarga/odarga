SELECT title FROM movies JOIN stars ON movies.id = stars.movie_id JOIN people ON stars.person_id = people.id JOIN ratings ON ratings.movie_id = movies.id
WHERE name = 'Chadwich Bosemar' ORDER BY rating DESC LIMIT 5;
