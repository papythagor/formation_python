import os

chemin = "/home/papyloup/Documents/prog/essai"
dossier = os.path.join(chemin,"dossier")
if not os.path.exists(dossier):
    os.makedirs(dossier,exist_ok=True) #si pas de boucle conditionnelle
else:
    print("Dossier déjà existant.")
    os.removedirs(dossier)