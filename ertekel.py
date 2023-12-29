



def Ertekeles():
	nap = str(input("Add meg a napot: "))
	ora = str(input("Add meg az óra nevét: "))
	jegy = int(input("Add meg az érdemjegyet (0-5): "))

	if jegy < 0:
		ertekeles = "Az értékelés nem lehet negatív!"
	elif jegy > 5:
		ertekeles = "5 pont feletti értékelés nem elfogadható!"
	else:
		ertekeles = "Köszönjük az értékelést!"

	return nap, ora, jegy, ertekeles



































