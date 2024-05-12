# 1. Feladat - Adatok beolvasása, nem szükséges képernyőre írás

with open("utca.txt", "r") as file:

    elsosor = file.readline().strip().split()
    a_sav = int(elsosor[0])
    b_sav = int(elsosor[1])
    c_sav = int(elsosor[2])

    adoszam = []
    utca = []
    hazszam = []
    adosav = []
    terulet = []

    for sor in file:
        sor = sor.strip().split()
        adoszam.append(sor[0])
        utca.append(sor[1])
        hazszam.append(sor[2])
        adosav.append(sor[3])
        terulet.append(int(sor[4]))

hossz = len(adoszam)


print("2. feladat.", end=" ")
print(f"A mintában {hossz} telek szerepel.")


print("3. feladat.", end=" ")

tulajszam = input("Egy tulajdonos adószáma: ").strip()
szerepel = False

for i in range(hossz):
    if adoszam[i] == tulajszam:
        print(f"{utca[i]} utca {hazszam[i]}")
        szerepel = True

if szerepel == False:
    print("Nem szerepel az adatállományban.")


# 4. Feladat - Függvény elkészítése

def ado(adosav, alapterulet):

    ertek = 0

    if adosav == 'A':
        ertek = alapterulet * a_sav
    if adosav == 'B':
        ertek = alapterulet * b_sav
    if adosav == 'C':
        ertek = alapterulet * c_sav
    if ertek < 10000:
        ertek = 0

    return ertek


print("5. feladat")

a_ado = [0, 0]
b_ado = [0, 0]
c_ado = [0, 0]

for i in range(hossz):
    if adosav[i] == 'A':
        a_ado[0] += 1
        a_ado[1] += ado('A', terulet[i])
    if adosav[i] == 'B':
        b_ado[0] += 1
        b_ado[1] += ado('B', terulet[i])
    if adosav[i] == 'C':
        c_ado[0] += 1
        c_ado[1] += ado('C', terulet[i])

print(f"A sávba {a_ado[0]} telek esik, az adó {a_ado[1]} Ft.")
print(f"B sávba {b_ado[0]} telek esik, az adó {b_ado[1]} Ft.")
print(f"C sávba {c_ado[0]} telek esik, az adó {c_ado[1]} Ft.")


print("6. feladat")

tobbsav = []

for i in range(hossz-1):
    if utca[i] == utca[i+1] and adosav[i] != adosav[i+1]:
        if utca[i] not in tobbsav:
            tobbsav.append(utca[i])
            print(utca[i])


# 7. Feladat - Fájl írása, nem szükséges képernyőre írás

with open("fizetendo.txt", "w") as outfile:

    unique_adoszamok = []
    fizetendok = []
    e = 0

    for i in range(hossz):
        if adoszam[i] not in unique_adoszamok:
            unique_adoszamok.append(adoszam[i])

    for i in range(len(unique_adoszamok)):
        for j in range(hossz):
            if unique_adoszamok[i] == adoszam[j]:
                e += ado(adosav[j], terulet[j])
        
        outfile.write(f"{unique_adoszamok[i]} {e}\n")
        e = 0