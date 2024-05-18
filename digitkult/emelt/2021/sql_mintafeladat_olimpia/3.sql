SELECT DISTINCT orszagok.orszag FROM orszagok, versenyzok, eredmenyek
WHERE orszagok.azon = versenyzok.orszag_azon
AND versenyzok.azon = eredmenyek.versenyzo_azon
AND eredmenyek.helyezes = '1';