mdp = "votre mot de passe est trop court."
mot_de_passe = input("Veuillez entrer votre mot de passe : (minimum 8 caractères) ")

if len(mot_de_passe)==0:
    print(mdp.upper())
elif len(mot_de_passe)<8 and len(mot_de_passe)>0:
    print(mdp.capitalize())
elif mot_de_passe.isdigit()==True:
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")


