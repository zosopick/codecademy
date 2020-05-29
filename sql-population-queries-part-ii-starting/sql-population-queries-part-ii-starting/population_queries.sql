-- How many entries in the database are from Africa?
SELECT COUNT(*) AS 'Number of countries in Africa'
FROM countries
WHERE continent='Africa';



-- What was the total population of Oceania in 2005?
SELECT SUM(population)
AS ' Total population of Oceania in 2005'
FROM population_years
JOIN countries 
ON population_years.country_id=countries.id
WHERE continent='Oceania'
AND year=2005;



-- What is the average population of countries in South America in 2003?
SELECT AVG(population)
AS'Average population of countries in South America in 2003'
FROM population_years
JOIN countries
ON population_years.country_id=countries.id
WHERE continent='South America'
AND year=2003;



-- What country had the smallest population in 2007?
SELECT countries.name 
AS 'Country with the smallest population in 2007' ,
MIN(population)
AS 'Population'
FROM population_years
JOIN countries
ON population_years.country_id=countries.id
WHERE year=2007;



-- What is the average population of Poland during the time period covered by this dataset?
SELECT countries.name, AVG(population_years.population) AS "Average population of Poland from 2000-2010"
FROM countries JOIN population_years
ON countries.id =
population_years.country_id
WHERE countries.name = 'Poland';



-- How many countries have the word "The" in their name?
SELECT COUNT(*)
AS 'Number of countries that have the word "The" in their name.'
FROM population_years
JOIN countries
ON population_years.country_id=countries.id
WHERE name LIKE '%The%';



-- What was the total population of each continent in 2010?
SELECT countries.continent,
SUM(population_years.population)
AS'Total population of each continent in 2010'
FROM population_years
JOIN countries
ON population_years.country_id=countries.id
WHERE population_years.year=2010
GROUP BY 1;
