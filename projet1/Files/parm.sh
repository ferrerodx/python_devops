#!/bin/bash

echo "Les paramètres passés sont :"

# Boucle à travers les paramètres passés
for param in "$@"; do
    echo "\$${#}: $param"
done

