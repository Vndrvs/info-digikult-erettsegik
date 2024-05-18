SELECT orszagok.orszag FROM versenyzok, orszagok 
WHERE orszagok.azon = versenyzok.orszag_azon 
ORDER BY versenyzok.szul_dat DESC 
LIMIT 1;