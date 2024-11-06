#!/usr/bin/env python3
import sys

# Verifica se o número de parâmetros é igual a 1
if len(sys.argv) == 2:
    # Exibe a string em minúsculas
    print(sys.argv[1].lower())
else:
    # Se o número de parâmetros não for 1, exibe "none"
    print("none")
