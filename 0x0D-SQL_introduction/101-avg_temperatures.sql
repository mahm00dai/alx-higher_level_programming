-- avg_temperatures
SELECT city, AVG(value * 9/5 + 32) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
