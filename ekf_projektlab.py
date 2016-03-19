print ("Üdvözöllek a programban kérjük válassz milyen programot akarsz futtatni")
print("1 - Hello World")
print("2 - köszönő program")
print("3 - Négyzet kerület, terület")
print("4 - Téglalap kerület, terület")
print("5 - Pozitív/Negatív meghatározó")
print("6 - Páros/Páratlan meghatározó")
print("7 - Síknegyed meghatározó")
print("8 - Alap While ciklus (számok 1-10-ig)")
print("9 - Alap for ciklus (páros számok 0-100-ig")
print("10 - Prím Szám meghatározása")
print("------------------------------------------------")
print("0 - Kilépés")
valasztas=input("Választásom:")
muvelet=int(valasztas)
if(muvelet == 0):
    print("A program kilép!")
elif(muvelet == 1):
    #Hello World program -egyszerü szöveg kiírtás, minden programozási nyelv első programja
    print("Hello World")
    
elif(muvelet == 2):
    #Köszönő program - egy változót bekérünk és vele dolgozunk
    print("Köszönő program")
    nev = input("Add meg a neved:")
    print("Udvozollek,"+nev)
    
elif(muvelet == 3):
    #négyzet területét és kerületét mehatározó program
    print("Négyzet kerület és terület meghatározó program")
    a=input("Add meg az a oldal hosszát:")
    #type(a) - konvertálja az a változó értékét int típusúvá
    t=int(a)*int(a)
    print("A négyzet területe:"+str(t))
    k=4*int(a)
    print("A négyzet kerülete:"+str(k))
    
elif(muvelet == 4):
    #Téglalap területét és kerületét meghatározó program
    print("Téglalap kerület és terület meghatározó program")
    a=input("Add meg az a oldal hosszát:")
    b=input("Add meg a b oldal hosszát:")
    t=int(a)*int(b)
    print("A téglalap területe:"+str(t))
    k=2*(int(a)+int(b))
    print("A téglalap kerülete:"+str(k))
    
elif(muvelet == 5):
    #Egy számvizsgáló program ami eldönti egy bekért számról, hogy az pozitív-e vagy negatív
    print("Pozitív/Negatív szám meghatározó program")
    szam=input('Adjon meg egy számot:')
    if int(szam)>0 :
        print("A szám pozitív")
    elif int(szam)<0 :
        print("A szám negatív")

elif(muvelet == 6):
    #Páros páratlan meghatározó program
    print("Páros/Páratlan szám meghatározó program")
    vizsgalt_szam=input("Add meg a vizsgálandó számot:")
    if (int(vizsgalt_szam) % 2 == 0):
        print("A szám páros")
    else:
        print("A szám páratlan")
elif(muvelet == 7):
    #Síknegyed meghatározó
    print("Síknegyed meghatározó(add meg a koordinátákat):")
    x_koordinata=input("Add meg az x koordináta értékét: ")
    y_koordinata=input("Add meg az y koordináta értékét: ")
    x=int(x_koordinata)
    y=int(y_koordinata)
    if (x > 0 & y > 0):
        print("A pont az első síknegyedben van.")
    elif (x < 0 & y > 0):
        print("A pont az második síknegyedben van.")
    elif (x < 0 & y < 0):
        print("A pont az harmadik síknegyedben van.")
    elif (x > 0 & y < 0):
        print("A pont az megyedik síknegyedben van.")
    elif (x==0) :
        print("A pont az y tengelyen van.")
    elif (y==0) :
        print("A pont az x tengelyen van.")
    elif (x==0 & y==0) :
        print("A pont az origoban van.")
    else:
        print("Ilyen pont nem létezik")

elif(muvelet == 8):
    #while ciklus használata - első 10 szám kiíratása
    print("While ciklus használata, első 10 szám kiíratása a használatával")
    ciklusvaltozo=0
    while(ciklusvaltozo<10):
        ciklusvaltozo=ciklusvaltozo+1
        print(ciklusvaltozo)

elif(muvelet == 9):
    #for ciklus használata - páros számok kiíratása(0-100)
    print("For ciklus használata, páros számok kiíratása 0-20-ig")
    for i in range(11):
        print (i*2)
        
elif(muvelet == 10):
    #Prímszám vagy nem prímszám meghatározása for ciklusokkal    
    print ("Prímszám vagy nem prímszám")
    num = int(input("Add meg a maximumot: "))
    
    for n in range(2, num+1):
     for x in range(2, n):
         if n % x == 0:
            print (n, "nem prím mert", x, "*", n/x)
            break
     else:
          print (n, "Ez egy prímszám")