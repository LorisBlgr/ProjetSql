SELECT MAX(numVotes),primaryTitle
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst;