SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Romance'
ORDER BY numVotes DESC 
LIMIT 5;