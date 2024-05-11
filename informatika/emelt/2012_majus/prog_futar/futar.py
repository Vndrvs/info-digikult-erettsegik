# Note: Ezt a feladatot elég baltás módszerrel oldottam meg, több helyen érdemes lenne dictionary, illetve sort funkció használata pl,
# viszont nem vagyok benne biztos, hogy ezeket mindenki tanulta, így pl. inkább sorbarendezés tételt hoztam sort helyett.

# 1. feladat - Fájl beolvasása, képernyőre írás nem szükséges

with open("tavok.txt", "r") as file:

    nap = []
    fuvarszam = []
    km = []

    for sor in file:
        sor = sor.strip().split()
        nap.append(int(sor[0]))
        fuvarszam.append(int(sor[1]))
        km.append(int(sor[2]))

hossz = len(nap)

# Praktikus időrendbe helyezni az adatokat, ezt külön listákon teszem meg a sorbarendezés tétele szerint

sorted_nap = []
sorted_fuvarszam = []
sorted_km = []

for i in range(hossz):
    sorted_nap.append(nap[i])
    sorted_fuvarszam.append(fuvarszam[i])
    sorted_km.append(km[i])

for i in range(hossz-1):
    for j in range(i+1, hossz):
        if sorted_nap[i] > sorted_nap[j]:
            temp = sorted_nap[i]
            sorted_nap[i] = sorted_nap[j]
            sorted_nap[j] = temp

            temp = sorted_fuvarszam[i]
            sorted_fuvarszam[i] = sorted_fuvarszam[j]
            sorted_fuvarszam[j] = temp

            temp = sorted_km[i]
            sorted_km[i] = sorted_km[j]
            sorted_km[j] = temp

for i in range(hossz-1):
    for j in range(i+1, hossz):
        if sorted_nap[i] == sorted_nap[j] and sorted_fuvarszam[i] > sorted_fuvarszam[j]:
            temp = sorted_nap[i]
            sorted_nap[i] = sorted_nap[j]
            sorted_nap[j] = temp

            temp = sorted_fuvarszam[i]
            sorted_fuvarszam[i] = sorted_fuvarszam[j]
            sorted_fuvarszam[j] = temp

            temp = sorted_km[i]
            sorted_km[i] = sorted_km[j]
            sorted_km[j] = temp


print("2. feladat")
print(f"A hét legelső útja {sorted_km[0]} km hosszú volt.")


print()
print("3. feladat")
print(f"A hét utolsó útja {sorted_km[-1]} km hosszú volt.")


print()
print("4. feladat")
print("Heti szabadnap(ok):", end=" ")

hetnapjai = []

for i in range(7):
    hetnapjai.append(i+1)
    if hetnapjai[i] not in nap:
        print(hetnapjai[i], end=" ")


print()
print()
print("5. feladat")

maxx = 0
legtobb = 0

for i in range(hossz):
    if fuvarszam[i] > maxx:
        maxx = fuvarszam[i]
        legtobb = nap[i]

print(f"A legtöbb fuvar a hét {legtobb}. napján volt.")


print()
print("6. feladat")

futar_napok = []
fuvarkm = []

for i in range(7):
    futar_napok.append(i+1)
    fuvarkm.append(0)

for i in range(len(futar_napok)):
    for j in range(hossz):
        if futar_napok[i] == nap[j]:
            fuvarkm[i] += km[j]
    print(f"{futar_napok[i]} nap: {fuvarkm[i]} km")


def dijkalkulator(uthossza):

    dij = 0
    if uthossza <= 2:
        dij = 500
    elif uthossza <= 5:
        dij = 700
    elif uthossza <= 10:
        dij = 900
    elif uthossza <= 20:
        dij =  1400
    elif uthossza <= 30:
        dij = 2000
    else:
        dij = "-érvénytelen-"

    return dij


print()
print("7. feladat")

userdata = int(input("A kalkulációhoz kérem adja meg a távolságot (kilométerben): "))

print(f"A díjazás értéke: {dijkalkulator(userdata)} Ft.")

# 8. feladat - Fájl elkészítése, képernyőre írás nem szükséges
with open("dijazas.txt", "w") as outfile:
    for i in range(hossz):
        outfile.write(f"{sorted_nap[i]}. nap {sorted_fuvarszam[i]}. út: {dijkalkulator(sorted_km[i])} Ft\n")


print()
print("9. feladat")

summa_osszeg = 0

for i in range(hossz):
    summa_osszeg += dijkalkulator(km[i])

print(f"A futár a heti munkájáért {summa_osszeg} Forintot kap.")