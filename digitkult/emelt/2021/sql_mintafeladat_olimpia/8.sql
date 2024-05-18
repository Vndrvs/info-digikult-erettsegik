CREATE TABLE pont_tabla1 
SELECT orszagok.orszag, 
erem_tabla.arany * 3 + erem_tabla.ezust * 2 + erem_tabla.bronz AS pontszam
FROM orszagok, erem_tabla 
WHERE erem_tabla.orszag_azon = orszagok.azon
HAVING pontszam >= 20;