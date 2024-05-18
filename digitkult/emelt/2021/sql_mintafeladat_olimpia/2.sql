SELECT versenyszamok.versenyszam, eredmenyek.helyezes, eredmenyek.megjegyzes AS idoeredmeny 
FROM versenyzok, eredmenyek, versenyszamok
WHERE versenyzok.azon = eredmenyek.versenyzo_azon 
AND eredmenyek.versenyszam_azon = versenyszamok.azon
AND versenyzok.nev = 'Vajda Attila';