SELECT primaryTitle,numVotes,averageRating
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE averageRating>=9 AND numVotes>=10000;