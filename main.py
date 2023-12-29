

import ertekel
import sorozat
import hatoslotto





# Feladat 1.
nap, ora, jegy, ertekeles = ertekel.Ertekeles()


print(f"I/A, B:\n\tHét napja: {nap}\n\tÓra neve: {ora}\n\tÉrtékelés (0-5): {jegy}")
print(f"I/C:\n\t{ertekeles}\n\tÖsszefoglaló: ’{nap}’, ’{ora}’, {jegy} érték")





# Feladat 2.
sorozat.VeletlenSzamok()

sorozat.konzol_ir()

sorozat.fajlba_ir()







# Feladat 3.
huzasok = hatoslotto.HuzasokSzama()
print(f"III/A, B:\n\n\tA húzások száma: {huzasok}")


atlag = hatoslotto.NegyvenkettoAtlag()
print(f"\nIII/C:\n\n\tA 43. héten húzott számok átlaga: {atlag}")


adat = hatoslotto.LegnagyobbAdatai()
print(f"\nIII/D:\n\n\tAz első legnagyobb kihúzott szám értéke: {round(adat[0])}, {adat[1]}-ben, a {adat[2]}. héten húzták ki, ez volt a {adat[3]}. húzás. ")























