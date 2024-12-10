-- avg_temperatures
SELECT city, 
       ROUND(AVG((value * 9 / 5) + 32), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
