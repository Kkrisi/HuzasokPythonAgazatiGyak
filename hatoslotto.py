

from HuzasClass import Huzas



def fajlBeolvasas():
	fajl = open("huzasok.txt","r",encoding="UTF-8")
	fajl.readline()
	sorokLista = fajl.readlines()
	fajl.close()

	huzasLista = []
	for i in range(0,len(sorokLista),1):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split('@')
		huzas = int(sorLista[0])
		ev = int(sorLista[1])
		het = int(sorLista[2])
		szam = float(sorLista[3])

		huzas = Huzas(huzas,ev,het,szam)
		huzasLista.append(huzas)

	return huzasLista




def HuzasokSzama():
	lista = fajlBeolvasas()
	db = 0
	for huzas in lista:
		db += 1
	return db






def NegyvenkettoAtlag():
	lista = fajlBeolvasas()
	osszeg = 0
	szamlalo = 0
	for i in range(0,len(lista),1):
		if lista[i].het == 42:
			osszeg += lista[i].szam
			szamlalo += 1
	return round(osszeg / szamlalo, 2)





def LegnagyobbAdatai():
	lista = fajlBeolvasas()
	legn = 0
	adatok = 0
	for i in range(0,len(lista),1):
		if lista[i].szam > legn:
			legn = lista[i].szam
			adatok = lista[i].szam, lista[i].ev, lista[i].het, lista[i].huzas 
	return adatok




















