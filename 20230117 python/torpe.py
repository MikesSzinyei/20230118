file=open("torpek.csv","r", encoding="UTF-8")
kova=open("kova.csv","w", encoding="UTF-8")
magaslany=open("magaslany.csv", "w",encoding="UTF-8")

sorokSzama=-1
fiuk=0
nok=0
kover=0
suly=0

max=0
magassag=0
magastorpe=""

min=2000000
alacsony=0
alacsontrope=""

sor=next(file)
for sor in file:
    
    elemek=sor.split(";")
    for i in range(len(elemek)):
        elemek[i]=elemek[i].strip('\" ')


    if elemek[2]=="Kova":
        kova.write (str(elemek))

    if elemek[3]=="F":
        fiuk+=1

    if elemek[3]=="N":
        nok+=1

    if int(elemek[4])>60:
        kover+=1

    if int(elemek[5])>max:
        max=int(elemek[5])
        magastorpe=elemek[1]

    if int(elemek[5])<min:
        min=int(elemek[5])
        alacsontrope=elemek[1]

    if int(elemek[5])>=140 and elemek[3]=="F":
        magaslany.write (str(elemek))

    suly+=int(elemek[4])
    sorokSzama+=1



    
    

file.close()


print("A rekordok száma:",sorokSzama)
print("A fiuk száma:",fiuk)
print("A nok száma:",nok)
print("A kövérek száma:",kover)
print("A törpék súlya:",suly)
print("A törpék A legmagasabb törpe:",magastorpe,"a magassága:", max )
print("A törpék A legalacsonyabb törpe:",alacsontrope,"a magassága:", min )
