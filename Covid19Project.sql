--LOOKING AT THE GENERAL OVERVIEW OF THE (COVIDDEATH) TABLE USING THE SELECT ALL STATEMENT---

SELECT * 
FROM CovidDeaths;


---LOOKING AT THE CONTINENTS WHICH HAS THE HIGHEST INFECTION 

SELECT 
continent, 
MAX(total_cases) AS Continents_with_high_infection
FROM CovidDeaths
WHERE total_cases IS NOT NULL AND
continent IS NOT NULL
GROUP BY continent
ORDER BY MAX(total_cases) DESC;


--LOOKING AT TOTAL THE DEATH PERCENTAGE IN CONTINENTS

SELECT continent, Date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS Death_percentage
FROM CovidDeaths
WHERE continent IS NOT NULL AND
total_cases IS NOT NULL AND
total_deaths IS NOT NULL
ORDER BY 1,2 DESC;


--LOOKING AT PERCENTAGE OF PEOPLE INFECTED IN CONTINENTS

SELECT continent,population,MAX(CAST(total_cases AS INTEGER)) AS infections_count,MAX((total_cases/population))*100 AS percentage_of_population_infected
FROM CovidDeaths
WHERE continent IS NOT NULL AND
population IS NOT NULL AND
total_cases IS NOT NULL 
GROUP BY continent,population
ORDER BY percentage_of_population_infected DESC;

--LOOKING AT DEATH RATE PER POPULATION IN CONTINENTS---

SELECT continent,MAX(CAST(total_deaths AS INTEGER)) AS Death_count
FROM CovidDeaths
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY Death_count DESC ;

--JOINNING COVIDVACCINATIONS TABLE ON COVIDDEATHS TABLE AND LOOKING AT TOTAL POPULATION VS VACCINATIONS---
                      ---USE COMMON TABLE EXPRESSION(CTE)---

WITH population_vs_vaccination (continent, location, date, population,Rolling_people_vaccinated,new_vaccinations)
AS
(
SELECT CovidDeaths.continent, CovidDeaths.location,CovidDeaths.date, CovidDeaths.population, Covidvaccinations.new_vaccinations,
SUM(CONVERT(BIGINT,Covidvaccinations.new_vaccinations)) OVER (PARTITION BY CovidDeaths.location ORDER BY CovidDeaths.location, CovidDeaths.date) 
AS Rolling_people_vaccinated
FROM CovidDeaths
JOIN Covidvaccinations 
ON CovidDeaths.location = Covidvaccinations.location
AND CovidDeaths.date = Covidvaccinations.date
WHERE CovidDeaths.continent IS NOT NULL AND
new_vaccinations IS NOT NULL
)

SELECT * ,
(Rolling_people_vaccinated/population)*100
FROM population_vs_vaccination ;







