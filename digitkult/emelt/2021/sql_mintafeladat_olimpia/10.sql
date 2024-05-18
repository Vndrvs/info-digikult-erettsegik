UPDATE versenyzok 
SET versenyzok.szul_hely = (SELECT orszagok.fovaros 
                            FROM orszagok 
                            WHERE orszagok.azon = versenyzok.orszag_azon)
WHERE versenyzok.egyen_csapat = 'c';