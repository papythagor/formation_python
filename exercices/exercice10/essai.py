import random

nombre_mystere = random.randint(0,10)

nombre = input("Entrez un nombre ? ")

if(int(nombre)<nombre_mystere):
    print(f"Le nombre mystère est plus grand que {nombre}.")
elif(int(nombre)>nombre_mystere):
    print(f"Le nombre mystère est plus petit que {nombre}.")
else:
    print(f"Vous avez trouvé le nombre mystère.")