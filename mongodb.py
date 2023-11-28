# Appelleer pymongo
import pymongo
# La connexion du serveur et au base de donné
serveur = pymongo.MongoClient("mongodb://localhost:27017/")
db = serveur["premier"]
collect = db["oui"]
# Une fonction pour créer les informations
def information():
    nom = input("Votre nom:")
    prenom = input("Votre prénom:")
    email = input("Votre adresse email:")
    mot_de_passe = input("Votre mot de passe:")
    # Créer l'utilisateur en format json
    utilisateur ={
        "Nom": nom,
        "Prenom": prenom,
        "Email": email,
        "Mot de passe": mot_de_passe
    }
    # La commande pour créer l'utilisateur
    collect.insert_one(utilisateur)
    collect.insert_id 
# Liste des utilsateurs dans la base de donnée
def consulter_utilisateurs():
    for x in collect.find():
        print("Liste de l'utilisateur:",x)
def maj():
    # Identifiant de l'utilisateur à mettre à jour
    identifiant_utilisateur = input("identifiant_de_l_utilisateur:")
    # Nouveau mot de passe à définir
    nouveau_mot_de_passe = "nouveau_mot_de_passe"
    # Mettre à jour le mot de passe de l'utilisateur dans la base de données
    collect.update_one(
            {"_id": identifiant_utilisateur},
            {"$set": {"mot_de_passe": nouveau_mot_de_passe}}
        )
# Supprimer un utilisateur dans la base de donnée
def suprimer():
    # Identifiant de l'utilisateur à supprimer
    identifiant_utilisateur = input("Identifiant du compte à supprimer : ")
    # Vérifier si l'identifiant de l'utilisateur existe
    utilisateur = collect.find_one({"_id": identifiant_utilisateur})
    if utilisateur:
        # Créer la requête pour supprimer l'utilisateur avec cet identifiant
        myquery = { "_id": identifiant_utilisateur }
        # Supprimer l'utilisateur correspondant à cet identifiant
        x = collect.delete_one(myquery)
        # Afficher le nombre de comptes supprimés
        print(x.deleted_count, "documents supprimé.")
    else:
        print("Suite a un problème venant de ma part")
# Créaction de notre menu graphique
def menu():
    while True:
        print("Menu:")
        info = int(input("1.Ajouter,2.lister,3.Mettre à jour,4.Supprimer:"))
        if info == 1:
            information()
            break
        elif info == 2:
            consulter_utilisateurs()
            break
        elif info == 3:
            maj()
            break
        elif info == 4:
            suprimer()
            break
        else: 
            print("Choix invalide, veuillez réessayer.")
menu()