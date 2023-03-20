while True:
    try:
        numero1 = int(input("Inserisci il primo numero: "))
        break
    except ValueError:
        print("Devi inserire un numero intero, riprova.")

while True:
    numero2 = input("Inserisci il secondo numero: ")
    if numero2.isdigit():
        numero2 = int(numero2)
        break
    else:
        print("Devi inserire un numero intero, riprova.")
   
print("Il primo numero inserito è:", numero1)
print("Il secondo numero inserito è:", numero2)
