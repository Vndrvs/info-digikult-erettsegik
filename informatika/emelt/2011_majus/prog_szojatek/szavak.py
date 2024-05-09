print("1. feladat", end=" ")

maganhangzok = ['a', 'e', 'i', 'o', 'u']

beszo = input("Adjon meg egy szót: ")
van = False

for betu in beszo:
    if betu in maganhangzok:
        van = True

if van:
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.")


print()
print("2. feladat")

with open("szoveg.txt", "r") as file:

    szavak = []
    for sor in file:
        sor = sor.strip()
        szavak.append(sor)

hossz = len(szavak)

maxx_hossz = 0

for szo in szavak:
    if len(szo) > maxx_hossz:
        maxx_hossz = len(szo)
        maxx_szo = szo

print(f"A leghosszabb szó: {maxx_szo} - Ez a szó {maxx_hossz} karakterből áll.")


print()
print("3. feladat")

fit_counter = 0
maganhang = 0
massalhang = 0

for i in range(hossz):
    vizsgalt = list(szavak[i])
    for j in range(len(vizsgalt)):
        if vizsgalt[j] in maganhangzok:
            maganhang +=1
        if vizsgalt[j] not in maganhangzok:
            massalhang += 1
    
    if maganhang > massalhang:
        fit_counter += 1
        print(szavak[i], end=" ")

    maganhang = 0
    massalhang = 0


ratio = "{:.2f}".format((fit_counter/hossz)*100)

print()
print(f"{fit_counter}/{hossz} : {ratio}%")


print()
print("4. feladat")

otkarakter = []

for szo in szavak:
    if len(szo) == 5:
        otkarakter.append(szo)

bereszlet = list(input("Kérem adjon meg egy 3 karakteres szórészletet: "))

for word in otkarakter:
    if word[1] == bereszlet[0] and word[2] == bereszlet[1] and word[3] == bereszlet[2]:
        print(word, end=" ")


# 5. feladat - a feladat szövege szerint képernyőre írás nem szükséges (csak fájlt írunk)

letra = []
counter = 0

for i in range(len(otkarakter)):
    current_szo = otkarakter[i]
    for i in range(otkarakter.index(otkarakter[i]), len(otkarakter)):
        if current_szo[1:-1] == otkarakter[i][1:-1]:
            letra.append(otkarakter[i])
            counter += 1
    if counter == 1:
        letra.pop()
    elif counter > 1:
        letra.append("")

    counter = 0

with open("letra.txt", "w") as outfile:

    for szo in letra:
        outfile.write(szo)
        outfile.write("\n")