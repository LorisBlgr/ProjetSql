
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
