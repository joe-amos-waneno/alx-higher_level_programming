-- display the avg temprature by city
-- order by temp in descending order

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
