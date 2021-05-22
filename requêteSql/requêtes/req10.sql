SELECT primaryName,primaryProfession,originalTitle
FROM title_basics
JOIN name_titles ON knownForTitles = tconst
JOIN name_basics ON name_basics.nconst = name_titles.nconst
AND originalTitle="Star Wars: Episode VI - Return of the Jedi"
AND titleType = "movie";