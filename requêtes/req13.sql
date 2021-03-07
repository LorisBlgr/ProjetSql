SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Animation' AND numVotes>1000
ORDER BY numVotes DESC 
LIMIT 10;