SELECT primaryName, primaryTitle
FROM name_basics, title_basics
JOIN title_principals ON title_principals.nconst = name_basics.nconst
WHERE title_principals.tconst = title_basics.tconst
AND category = "director"
AND title_basics.tconst IN(SELECT title_basics.tconst
FROM title_basics
JOIN title_ratings ON title_ratings.tconst = title_basics.tconst
WHERE titleType = "movie"
ORDER BY averageRating DESC
LIMIT 5)