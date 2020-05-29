SELECT DISTINCT year AS  'Distinct years from this database' 
FROM population_years ;



SELECT MAX(population) 'Largest poulation size for Gabon in this dataset.' 
FROM  population_years;



SELECT country, population AS ' Population in 2005'
FROM population_years
WHERE year=2005
ORDER BY population ASC
LIMIT 10;



SELECT DISTINCT country AS 'Countries with a population of over 100 000 000 in 2010'
FROM population_years
WHERE population>100;


SELECT COUNT( DISTINCT country)  
AS ' Number of countries with "Islands" in their name'
FROM population_years
WHERE country LIKE '%Islands%';


SELECT ((
SELECT population FROM population_years
WHERE year=2010 AND country='Indonesia')-
(SELECT population FROM population_years
WHERE year=2000 AND country='Indonesia'))
AS 'Difference in Indonesias population 2000-2010';

