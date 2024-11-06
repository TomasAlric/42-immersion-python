#!/usr/bin/env python3
import sys

# Verificar se não há parâmetros
if len(sys.argv) == 1:
    print("none")
else:
    # Exibir o número de parâmetros
    print(f"parameters: {len(sys.argv) - 1}")

    # Usar o loop 'for' para iterar pelos parâmetros
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
