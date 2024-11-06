#!/usr/bin/env python3
import sys

# Verificar se o número de parâmetros é diferente de 1
if len(sys.argv) != 2:
    print("none")
else:
    # Pegar a string passada como parâmetro
    input_string = sys.argv[1]

    # Contar a quantidade de 'z' (minúsculo) na string
    z_count = input_string.count('z')

    # Se não houver 'z', imprimir "none"
    if z_count == 0:
        print("none")
    else:
        # Imprimir "z" para cada ocorrência de 'z'
        print('z' * z_count)
