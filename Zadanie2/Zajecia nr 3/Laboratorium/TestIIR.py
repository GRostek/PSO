import iir


wspolczynnikia1 = [1,2,3,1,1,1]
wspolczynnikib1 = [0.9,0.4,0.2,0.1]

wspolczynnikia2 = [1,0,1,0,1]
wspolczynnikib2 = [0.9,0.4,0.2,0.1]

wspolczynnikia3 = [1,0.5,0.25,0.125]
wspolczynnikib3 = [0.125,0.25,0.5,1,2,3]

sygnal_we_dirac = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sygnal_wy_dirac1 = []
sygnal_wy_dirac2 = []
sygnal_wy_dirac3 = []

sygnal_we_skokj = [0,0,0,0,1,1,1,1]
sygnal_wy_skokj1 = []
sygnal_wy_skokj2 = []
sygnal_wy_skokj3 = []

sygnal_we_naprz = [1,1,1,1,1,-1,-1,-1,-1,-1]
sygnal_wy_naprz1 = []
sygnal_wy_naprz2 = []
sygnal_wy_naprz3 = []


filtrIIR1 = iir.systemIIR(wspolczynnikia1, wspolczynnikib1)
filtrIIR2 = iir.systemIIR(wspolczynnikia2, wspolczynnikib2)
filtrIIR3 = iir.systemIIR(wspolczynnikia3, wspolczynnikib3)

for i in range(len(sygnal_we_dirac)):
    y = filtrIIR1.Wylicz(sygnal_we_dirac[i])
    sygnal_wy_dirac1.append(y)

    y = filtrIIR2.Wylicz(sygnal_we_dirac[i])
    sygnal_wy_dirac2.append(y)

    y = filtrIIR3.Wylicz(sygnal_we_dirac[i])
    sygnal_wy_dirac3.append(y)


#zerujemy dane w filtrach aby nie tworzyć ich od nowa
filtrIIR1.WyzerujDane()
filtrIIR2.WyzerujDane()
filtrIIR3.WyzerujDane()

for i in range(len(sygnal_we_skokj)):
    y = filtrIIR1.Wylicz(sygnal_we_skokj[i])
    sygnal_wy_skokj1.append(y)

    y = filtrIIR2.Wylicz(sygnal_we_skokj[i])
    sygnal_wy_skokj2.append(y)

    y = filtrIIR3.Wylicz(sygnal_we_skokj[i])
    sygnal_wy_skokj3.append(y)

filtrIIR1.WyzerujDane()
filtrIIR2.WyzerujDane()
filtrIIR3.WyzerujDane()

for i in range(len(sygnal_we_naprz)):
    y = filtrIIR1.Wylicz(sygnal_we_naprz[i])
    sygnal_wy_naprz1.append(y)

    y = filtrIIR2.Wylicz(sygnal_we_naprz[i])
    sygnal_wy_naprz2.append(y)

    y = filtrIIR3.Wylicz(sygnal_we_naprz[i])
    sygnal_wy_naprz3.append(y)


print("Filtr 1")
print("Wspolczynniki a: " + str(wspolczynnikia1))
print("Wspolczynniki b: " + str(wspolczynnikib1))
print()
print("delta diraca, wejscie: "+str(sygnal_we_dirac))
print("odp systemu: " + str(sygnal_wy_dirac1))
print()
print("skok jednostkowy, wejscie: "+str(sygnal_we_skokj))
print("odp systemu: " + str(sygnal_wy_skokj1))
print()
print("sygnal naprzemienny, wejscie: "+str(sygnal_we_naprz))
print("odp systemu: " + str(sygnal_wy_naprz1))
print()
print()

print("Filtr 2")
print("Wspolczynniki a: " + str(wspolczynnikia2))
print("Wspolczynniki b: " + str(wspolczynnikib2))
print()
print("delta diraca, wejscie: "+str(sygnal_we_dirac))
print("odp systemu: " + str(sygnal_wy_dirac2))
print()
print("skok jednostkowy, wejscie: "+str(sygnal_we_skokj))
print("odp systemu: " + str(sygnal_wy_skokj2))
print()
print("sygnal naprzemienny, wejscie: "+str(sygnal_we_naprz))
print("odp systemu: " + str(sygnal_wy_naprz2))
print()
print()


print("Filtr 3")
print("Wspolczynniki a: " + str(wspolczynnikia3))
print("Wspolczynniki b: " + str(wspolczynnikib3))
print()
print("delta diraca, wejscie: "+str(sygnal_we_dirac))
print("odp systemu: " + str(sygnal_wy_dirac3))
print()
print("skok jednostkowy, wejscie: "+str(sygnal_we_skokj))
print("odp systemu: " + str(sygnal_wy_skokj3))
print()
print("sygnal naprzemienny, wejscie: "+str(sygnal_we_naprz))
print("odp systemu: " + str(sygnal_wy_naprz3))

    
