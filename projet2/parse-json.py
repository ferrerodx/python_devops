import os
import json

def parser(repertoire="."):
    fichiers_json = [f for f in os.listdir(repertoire) if f.endswith(".json")]
    if not fichiers_json:
        print(f"Aucun fichier JSON trouvé dans le répertoire {repertoire}.")
        return None

    fichier_json = fichiers_json[0]
    chemin_absolu = os.path.abspath(os.path.join(repertoire, fichier_json))
    print(f"Chemin absolu du premier fichier JSON trouvé ({fichier_json}) : {chemin_absolu}")
    # Lire et analyser le fichier JSON
    with open(chemin_absolu, 'r') as json_file:
        data = json.load(json_file)

    # Extrait et affiche la valeur associée à la clé 'name'
    name_value = data.get('name', 'Clé non trouvée')
    print("Valeur associée à la clé 'name' :", name_value)

    # Parcourir toutes les clés et valeurs du dictionnaire JSON
    print("\nParcours de toutes les clés et valeurs du fichier JSON:")
    for key, value in data.items():
        print(f"Clé: {key}, Valeur: {value}")

# Exemple d'utilisation
repertoire_courant = "."  # Vous pouvez spécifier le répertoire souhaité ici
parser(repertoire_courant)
