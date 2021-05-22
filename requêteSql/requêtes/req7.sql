SELECT primaryTitle
FROM title_writers
JOIN title_basics ON title_writers.tconst = title_basics.tconst
WHERE writers=619923;
