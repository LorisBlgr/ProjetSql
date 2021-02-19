
requ3.sql
#03.Combien y a-t-il de titres dans cette base de données ?
SELECT COUNT(primaryName)
FROM name_basics ;

requ4.sql
#04.En quelle année est sortie le film The Godfather ?
SELECT startYear
FROM title_basics
WHERE primaryTitle="The Godfather" ;

requ5.sql
#05.En quelle année est sortie le premier film Superman ?
SELECT startYear
FROM title_basics
WHERE primaryTitle="Superman" ;

requ6.sql
#06.Quel est le titre original du film 'Les dents de la mer' ?
SELECT originalTitle
FROM title_basics
WHERE primaryTitle="Jaws" ;

requ7.sql
#07.Quel est le métier d’Olivier Nakache ?
SELECT primaryProfession
FROM name_basics
WHERE primaryName="Olivier Nakache";

requ8.sql
#08.Quels sont les films d’Olivier Nakache ?
SELECT primaryTitle
FROM title_writers
JOIN title_basics ON title_writers.tconst = title_basics.tconst
WHERE writers=619923;

requ9.sql
#09.Quel est le film ayant recueilli le plus de votes ?
SELECT MAX(numVotes),primaryTitle
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst;

requ10.sql
#10.Qui a écrit le scénario du film Taxi sorti en 1998 ?
SELECT writers
FROM title_writers
WHERE tconst=152930 ;

requ11.sql
#11.Quelles sont les noms et rôles (category et job) des personnes intervenant dans la production du film Return of the Jedi ?
;

requ12.sql
#12.Quels sont les titres des films notés plus de 9 sur 10 avec plus de 10 000 votes ?
SELECT primaryTitle,numVotes,averageRating
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE averageRating>=9 AND numVotes>=10000;

requ13.sql
#13.Quelle sont les 5 comédies romantiques les mieux notées ?
SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Romance'
ORDER BY numVotes DESC 
LIMIT 5;

requ14.sql
#14.Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?
SELECT numVotes,primaryTitle,genres
FROM title_ratings
JOIN title_basics ON title_ratings.tconst = title_basics.tconst
WHERE genres='Animation' AND numVotes>1000
ORDER BY numVotes DESC 
LIMIT 10;

requ15.sql
#15.Combien de films durent plus de 3 heures ?
SELECT COUNT(primaryTitle)
FROM title_basics
WHERE runtimeMinutes>=180;
