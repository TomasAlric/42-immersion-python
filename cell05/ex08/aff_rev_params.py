#!/usr/bin/env python3
import sys

# Verifica se há pelo menos dois parâmetros
if len(sys.argv) > 1:
    # Exibe os parâmetros em ordem reversa
    for param in reversed(sys.argv[1:]):
        print(param)
else:
    # Se houver menos de dois parâmetros, exibe "none"
    print("none")
