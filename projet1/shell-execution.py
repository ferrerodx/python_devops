#!/usr/bin/python3

import subprocess
import sys

def execute_script(script_name, *params):
    # Commande à exécuter
    command = [f"./Files/{script_name}"] + list(params)

    # Execution de  la commande
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    # Affiche la sortie 
    print(f"Résultat de l'exécution de {script_name} :")
    print(result.stdout)


script_name = sys.argv[1]
params = sys.argv[2:]
execute_script(script_name, *params)
