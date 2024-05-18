SELECT orszagok.azon AS azonosito, orszagok.orszag AS nev, orszagok.terulet, orszagok.lakossag, orszagok.fovaros, orszagok.foldresz 
-- ez egyszerűsítve megoldható 'SELECT * FROM orszagok'-al is, viszont egyedi elnevezéseket használok a szebb külalak érdekében 
FROM orszagok
WHERE orszagok.foldresz = 'Európa'
AND orszagok.azon NOT IN (SELECT versenyzok.orszag_azon 
                          FROM versenyzok);