

import random


def VeletlenSzamok():
	global lista
	lista = []
	for szam in range(8):
		szam = random.randint(-100,859)
		lista.append(szam)



	print(f"\nII/A, B, C:\n\t")
	szamlalo = 0
	for eredmeny in lista:
		szamlalo += 1
		if szamlalo == len(lista):
			print(eredmeny,end="")
		else:
			if szamlalo == 1:
				print("\t",eredmeny,end=";")
			else:
				print(eredmeny,end=";")
		
	return lista






def tizzel_osztahatoak_szama():
	szamlalo = 0
	for szam in lista:
		if szam % 10 == 0:
			szamlalo += 1
	return round(szamlalo)






def konzol_ir():
	szam = tizzel_osztahatoak_szama()
	print(f"\n\nII/D, E:\n\n\tTízzel osztható számok száma: {szam}.")






def fajlba_ir():
	szam = tizzel_osztahatoak_szama()
	f = open('vegeredmeny.txt','w')
	f.write(f"II/F:\n\tTízzel osztható számok száma: {szam}.")
	f.close()





















