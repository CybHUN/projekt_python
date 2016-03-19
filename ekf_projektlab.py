#Hello World program -egyszerü szöveg kiírtás, minden programozási nyelv első programja
print("Hello World")

#Köszönő program - egy változót bekérünk és vele dolgozunk
print("--=Köszönő program=--")
nev = input("Add meg a neved:")
print("Udvozollek,"+nev)

#négyzet területét és kerületét mehatározó program
print("*--=Négyzet kerület és terület meghatározó program=--)
a=input("Add meg az a oldal hosszát:")
#type(a) - konvertálja az a változó értékét int típusúvá
t=int(a)*int(b)
print("A négyzet területe:"+str(t))
k=2*(int(a)+int(b))
print("A négyzet kerülete:"+str(k))

#Téglalap területét és kerületét meghatározó program
print("*--=Téglalap kerület és terület meghatározó program=--)
a=input("Add meg az a oldal hosszát:")
b=input("Add meg a b oldal hosszát:")
t=int(a)*int(b)
print("A téglalap területe:"+str(t))
k=2*(int(a)+int(b))
print("A téglalap kerülete:"+str(k))

#Egy számvizsgáló program ami eldönti egy bekért számról, hogy az pozitív-e vagy negatív
print("Pozitív/Negatív szám meghatározó program")
szam=input('Adjon meg egy számot:')
if int(szam)>0 :
    print("a szám pozitív")
elif int(szam)<0 :
    print("a szám negatív")

#Páros páratlan meghatározó program
print("Páros/Páratlan szám meghatározó program")
vizsgalt_szam=input("Add meg a vizsgálandó számot:")
if (int(vizsgalt_szam) % 2 == 0):
    print("A szám páros")
else:
    print("A szám páratlan")