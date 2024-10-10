print("Scegli la figura di cui calcolare il perimetro")
print("**********************************************\n")
print("1. Quadrato \n2. Cerchio \n3. Rettangolo")

scelta = 0
figure = ["quadrato", "cerchio", "rettangolo"]

while scelta not in (1, 2, 3):
	scelta = int(input("\nInserisci un numero > "))
	if scelta in (1, 2, 3):
		print("Ottimo, hai scelto il", figure[scelta-1] + ".\n")
	else:
		print("Inserisci una scelta valida.")

if scelta == 1:
	lato = float(input("Inserisci il lato del quadrato: "))
	print("Il perimetro del quadrato è ", lato*4)
elif scelta == 2:
	raggio = float(input("Inserisci il raggio del cerchio: "))
	print("La circonferenza del cerchio è ", raggio*3.14*2)
elif scelta == 3:
	base = float(input("Inserisci la base del rettangolo: "))
	altezza = float(input("Inserisci l'altezza del rettangolo: "))
	print("Il petrimetro del rettangolo è ", base*2+altezza*2)

print("\n**********************")
print("Programma terminato.")
