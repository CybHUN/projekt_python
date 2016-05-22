#somieri
#<<<<<<< HEAD
#Egyszerű függvények I: összeadás
def osszeadas(a,b):
    osszeg=a+b
    return osszeg
#Egyszerű függvények I: kivonás
def kivonas(a,b):
    kulonbseg=a-b
    return kulonbseg
#Egyszerű függvények I: szorzat
def szorzas(a,b):
    szorzat=a*b
    return szorzat
#Egyszerű függvények I: osztás
def osztas(a,b):
    hanyados=a/b
    return hanyados
#Random szám generáló függvény
def rand(also,felso):
    import random
    randomszam=random.randint(also,felso)
    return randomszam
#Lista feltöltő függvény
def lista_feltolto(meret):
    lista=[]
    szamlalo = 0
    while szamlalo < meret:
        lista.append(rand(1,100))
        szamlalo = szamlalo + 1
    return lista
#Lista kiírató függvény
def lista_kiirato(kiirando_lista,meret):
    for i in range(meret):
        print (kiirando_lista[i],",", end="")
#Összegzés tétele függvénnyel
def osszegzes(meret):
    osszeg=0
    osszeg_lista=lista_feltolto(meret)
    for i in range(meret):
        print (osszeg_lista[i],",", end="")
        osszeg=osszeg+osszeg_lista[i]
    print ("\nA lista elemeiek összege:",osszeg)
#Összegzés tétele függvénnyel
def atlagszamitas(meret):
    osszeg=0
    atlag_lista=lista_feltolto(meret)
    for i in range(meret):
        print (atlag_lista[i],",", end="")
        osszeg=osszeg+atlag_lista[i]
    print ("\nA lista elemeiek átlaga:",osszeg/meret)
#Megszámlálás tétele függvénnyel
def megszamlalas(meret):
    db=0
    megszamlalando_lista=lista_feltolto(meret)
    for i in range(meret):
        if (int(megszamlalando_lista[i]) % 2 == 0):
            db=db+1            
        print (megszamlalando_lista[i],",", end="")
    print ("\nA lista páros elemeiek száma:",db)
#Minimumkiválasztás tétele függvénnyel
def minimumkivalasztas(meret):
    minimumkivalasztos_lista=lista_feltolto(meret)
    min=minimumkivalasztos_lista[0]
    for i in range(meret):
        if (minimumkivalasztos_lista[i]<min):
            min=minimumkivalasztos_lista[i]         
        print (minimumkivalasztos_lista[i],",", end="")
    print ("\nA legkisebb elem:",min)
#Maximumkiválasztás tétele függvénnyel
def maximumkivalasztas(meret):
    maximumkivalasztos_lista=lista_feltolto(meret)
    max=maximumkivalasztos_lista[0]
    for i in range(meret):
        if (maximumkivalasztos_lista[i]>max):
            max=maximumkivalasztos_lista[i]         
        print (maximumkivalasztos_lista[i],",", end="")
    print ("\nA legnagyobb elem:",max)
#binomiális együttható kiszámítása
def binomialis(m,k):
    if ((k==0) | (k==m)):
        return 1
    else:
        return binomialis(m-1,k)+binomialis(m-1,k-1)
#=======
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
print("11 - Háromszög szerkeszthetősége")
print("12 - Egyszerű összeadás függvénnyel")
print("13 - A négy alapművelet függvénnyel")
print("14 - Random szám generálás függvénnyel 1-100")
print("15 - Random szám generálás függvénnyel beállítható")
print("16 - Tömb feltöltése és tömb elemeinek kiíratása függvénnyel")
print("17 - Összegzés tétele függvénnyel")
print("18 - Átlagszámítás tétele függvénnyel")
print("19 - Megszámlálás tétele függvénnyel")
print("20 - Minimum kiválasztás tétele függvénnyel")
print("21 - Maximum kiválasztás tétele függvénnyel")
print("22 - Legnagyobb közös osztót meghatározó program")
print("23 - Számtani vagy mértani sorozat-e?")
print("24 - faktoriális for ciklussal")
print("25 - két szám közül a nagyobb meghatározása")
print("26 - binomiális együttható kiszámítása")
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
    if (x > 0 | y > 0):
        print("A pont az első síknegyedben van.")
    elif (x < 0 | y > 0):
        print("A pont az második síknegyedben van.")
    elif (x < 0 | y < 0):
        print("A pont az harmadik síknegyedben van.")
    elif (x > 0 | y < 0):
        print("A pont az megyedik síknegyedben van.")
    elif (x==0 | y==0) :
        print("A pont az origoban van.")
    elif (x==0) :
        print("A pont az y tengelyen van.")
    elif (y==0) :
        print("A pont az x tengelyen van.")
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
elif(muvelet == 11):
    # Háromszög szerkeszthetőség vizsgálata
    print ("A háromszög szerkeszthető?")
    a = int(input("Add meg az a oldalt:"))
    b = int (input("Add meg az b oldalt:"))
    c = int (input("Add meg az c oldalt:"))
    if ((a + b > c) & (a + c > b) & (b + c > a)):
        print ("A háromszög szerkeszthető!")
    else:
        print ("A háromszög nem szerkeszthető!")
elif(muvelet == 12):
    # Két szám összeadása függvény segítségével
    elso_szam = int(input("Add meg az első számot:"))
    masodik_szam = int (input("Add meg a második számok:"))
    print ("az összeadás eserménye",osszeadas(elso_szam,masodik_szam))
elif(muvelet == 13):
    # Négy alapművelet elkészítése függvény segítségével
    elso_szam = int(input("Add meg az első számot:"))
    masodik_szam = int (input("Add meg a második számok:"))
    print ("Az összeadás eredménye",osszeadas(elso_szam,masodik_szam))
    print ("A kivonás eredménye",kivonas(elso_szam,masodik_szam))
    print ("A szorzás eredménye",szorzas(elso_szam,masodik_szam))
    print ("Az osztás eredménye",osztas(elso_szam,masodik_szam))
elif(muvelet == 14):
    #egyszerű random szám generálása 1 és 100 között
    print ("A generált random szám:",rand(1,100))
elif(muvelet == 15):    
    #random szám generálása az álltalunk megadott intervallumban
    hatar_egy = int(input("Add meg az első számot:"))
    hatar_ketto = int (input("Add meg a második számok:"))
    print ("A generált random szám:",rand(hatar_egy,hatar_ketto))
elif(muvelet == 16):
    lista_meret = int(input("Hány elemű tömböt hozzak létre?:"))
    lista_kiirato(lista_feltolto(lista_meret),lista_meret);
elif(muvelet == 17):
    elemszam = int (input("Hány elemű tömbnek adjuk össze az elemeit:"))
    osszegzes(elemszam);
elif(muvelet == 18):
    elemszam = int (input("Hány elemű tömbnek számoljuk ki az áltagás:"))
    atlagszamitas(elemszam);    
elif(muvelet == 19):
    elemszam = int (input("Hány elemű tömbben adjuk meg a páros számok számát:"))
    megszamlalas(elemszam); 
elif(muvelet == 20):
    elemszam = int (input("Hány elemű tömbben adjuk meg a minimumát:"))
    minimumkivalasztas(elemszam); 
elif(muvelet == 21):
    elemszam = int (input("Hány elemű tömbben adjuk meg a maximumát:"))
    maximumkivalasztas(elemszam);
elif(muvelet==22):
    print("Legnagyobb közös osztót meghatározó program")
    ea=int(input("Egyik szám: "))
    eb=int(input("Másik szám: "))
    eaa=int(ea)
    ebb=int(eb)
    if eaa<ebb:
        es=ea;
        ea=eb;
        eb=es;
        em=ea%eb
    while em>0:
        ea=eb
        eb=em
        em=ea%eb
    print("A legnagyobb közös osztó:"+str(eb))  
elif(muvelet==23):
    print("23 - Számtani vagy mértani sorozat-e?")
    sa1=int(input("a1 értéke: "))
    sa2=int(input("a2 értéke: "))
    sa3=int(input("a3 értéke: "))
    if((sa2-sa1)==(sa3-sa2)):
        print("számtani sorozat")
    elif((sa2/sa1)==(sa3/sa2)):
        print("mértani sorozat")
    else:
        print("egyik sem")
elif(muvelet==24):
    print("24 - faktoriális for ciklussal")
    fn=int(input("n értéke: "))
    if fn<0:
        print("n nem lehet nulla")
    elif fn==0:
        print('n faktoriálisa: 0')
    else:
        fe=1
        for i in range(1,fn+1):
            fe=fe*i
        print("n érétke:"+str(fe))
elif(muvelet==25):
    print("25 - két szám közül a nagyobb meghatározása")
    na=int(input("egyik szám: "))
    nb=int(input("másik szám: "))
    if na<nb:
        print("nagyobbik szám:"+str(nb))
    elif na>nb:
        print("nagyobbik szám"+str(na))
    else:
        print("a két szám egyenlő")
elif(muvelet==26):
    print("26 - binomiális együttható kiszámítása")
    k_ertek=int(input("adja meg k értékét: "))
    n_ertek=int(input("adja n értékét: "))
    if k_ertek>n_ertek:
        print("k nem lehet nagyobb n-nél")
    else:
        print("n alatt a k: ",binomialis(n_ertek,k_ertek))