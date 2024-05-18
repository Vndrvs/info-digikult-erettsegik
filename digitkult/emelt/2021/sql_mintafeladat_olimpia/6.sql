SELECT orszagok.foldresz, COUNT(orszagok.azon) AS orszagok, SUM(orszagok.lakossag) AS osszlakossag, AVG(orszagok.terulet) AS atlagterulet
FROM orszagok
WHERE orszagok.foldresz IS NOT NULL
GROUP BY orszagok.foldresz;