
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
#06.Quel est le titre original du film 'Les dents de la mer ? 
SELECT originalTitle
FROM title_basics
WHERE primaryTitle="Jaws" ;

requ7.sql
#07.Quel est le métier d’Olivier Nakache ? 
SELECT primaryProfession
FROM name_basics
WHERE primaryName="Olivier Nakache";

requ10.sql
#10. Qui a écrit le scénario du film Taxi sorti en 1998 ?
SELECT writers
FROM title_writers
WHERE tconst=152930 ;
