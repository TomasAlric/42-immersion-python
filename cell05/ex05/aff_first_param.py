#!/usr/bin/env python3
import sys

# Verifica se há parâmetros passados além do nome do script
if len(sys.argv) > 1:
    # Exibe o primeiro parâmetro
    print(sys.argv[1])
else:
    # Se não houver parâmetros, exibe "none"
    print("none")
