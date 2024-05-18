SELECT versenyzok.nev, versenyzok.szul_dat AS szuletett 
FROM versenyzok 
WHERE versenyzok.szul_dat >= '1980.01.01.' 
AND versenyzok.egyen_csapat = 'e' 
ORDER BY versenyzok.nev;