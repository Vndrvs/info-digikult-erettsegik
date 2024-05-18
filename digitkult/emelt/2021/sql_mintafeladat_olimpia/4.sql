SELECT versenyzok.nev, versenyzok.szul_hely AS orszag,
versenyzok.szul_dat AS szuletett
FROM versenyzok 
WHERE versenyzok.szul_dat > (SELECT versenyzok.szul_dat
                            FROM versenyzok 
                            WHERE versenyzok.nev = 'Cseh László');