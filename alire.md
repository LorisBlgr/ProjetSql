requ1.sql
#01.Quels sont les différents types de titres dans cette base de données ?
SELECT DISTINCT(titleType)
FROM title_basics

requ2.sql
#02.Combien y a-t-il de titres dans cette base de données ?
SELECT COUNT(primaryName)
FROM name_basics;

requ3.sql
#03.En quelle année est sortie le film The Godfather ?
SELECT startYear
FROM title_basics
WHERE primaryTitle="The Godfather";

requ4.sql
#04.En quelle année est sortie le premier film Superman ?
SELECT startYear
FROM title_basics
WHERE primaryTitle="Superman";

requ5.sql
#05.Quel est le titre original du film 'Les dents de la mer' ?
SELECT originalTitle
FROM title_basics
WHERE primaryTitle="Jaws";

requ6.sql
#06.Quel est le métier d’Olivier Nakache ?
SELECT primaryProfession
FROM name_basics
WHERE primaryName="Olivier Nakache";

requ7.sql
#07.Quels sont les films d’Olivier Nakache ?
SELECT primaryTitle
FROM title_writers
JOIN title_basics ON title_writers.tconst = title_basics.tconst
WHERE writers=619923;

requ8.sql
#08.Quel est le film ayant recueilli le plus de votes ?
SELECT MAX(numVotes),primaryTitle
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst;

requ9.sql
#09.Qui a écrit le scénario du film Taxi sorti en 1998 ?
SELECT writers
FROM title_writers
WHERE tconst=152930 ;

requ10.sql
#10.Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?
;

requ11.sql
#11.Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?
SELECT primaryTitle,numVotes,averageRating
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE averageRating>=9 AND numVotes>=10000;

requ12.sql
#12.Quelle sont les 5 comédies romantiques les mieux notées ?
SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Romance'
ORDER BY numVotes DESC 
LIMIT 5;

requ13.sql
#13.Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?
SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Animation' AND numVotes>1000
ORDER BY numVotes DESC 
LIMIT 10;

requ14.sql
#14.Combien de films durent plus de 3 heures ?
SELECT COUNT(primaryTitle)
FROM title_basics
WHERE runtimeMinutes>=180;

requ15.sql
#15.Quelle est la durée moyenne d’un film ?
SELECT AVG(runtimeMinutes) 
FROM title_basics 
WHERE titleType = 'movie';

requ16.sql
#16.Quel est le film le plus long ?
SELECT primaryTitle, MAX(runtimeMinutes) 
FROM title_basics;

requ17.sql
#17.Quels sont les 5 films les plus longs ?
SELECT originalTitle
FROM title_basics
WHERE titleType = "movie"
ORDER BY runtimeMinutes DESC
LIMIT 5

requ18.sql
#18.Quels sont les titres des films les plus connus de Sean Connery ?
SELECT originalTitle
FROM title_basics
JOIN name_titles ON knownForTitles = tconst
JOIN name_basics ON name_basics.nconst = name_titles.nconst
WHERE primaryName = "Sean Connery"
AND titleType = "movie"

requ19.sql
#19.Quels sont les acteurs ayant joué le rôle de James Bond, et dans quels films ?
SELECT primaryName, originalTitle
FROM name_basics, title_basics
JOIN title_principals ON title_principals.tconst = title_basics.tconst
WHERE title_principals.nconst = name_basics.nconst
AND characters LIKE "%James Bond%"
AND category = "actor"
AND titleType = "movie"

requ20.sql
#20.Quel sont les réalisateurs ayant fait les cinq film les mieux notés ? Indiquer les noms des films correspondants.
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

requ21.sql
#21.Quels sont les noms des épisodes de Game of Thrones ?
SELECT primaryTitle
FROM title_basics
JOIN title_episode ON title_episode.tconst = title_basics.tconst
WHERE parentTconst IN(SELECT title_basics.tconst
FROM title_basics
WHERE primaryTitle = "Game of Thrones"
AND titleType = "tvSeries")