SELECT versenyzok.nev 
FROM versenyzok 
WHERE versenyzok.azon IN 
  (SELECT csapattagok.versenyzo_azon 
   FROM csapattagok 
   WHERE csapattagok.csapat_azon = (
     SELECT v.azon 
     FROM versenyzok v
     JOIN orszagok o ON v.orszag_azon = o.azon 
     WHERE v.nev = 'Kézilabda női' 
       AND o.orszag = 'Magyarország'
     ) 
   ) 
ORDER BY versenyzok.nev DESC;