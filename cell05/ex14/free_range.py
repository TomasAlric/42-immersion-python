#!/usr/bin/env python3
import sys

# Verifica se o número de parâmetros é igual a 2
if len(sys.argv) != 3:
    print("none")
else:
    # Converte os parâmetros para inteiros
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    # Cria a lista com os valores no intervalo
    result = list(range(start, end + 1))

    # Exibe a lista
    print(result)
