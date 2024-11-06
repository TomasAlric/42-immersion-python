#!/usr/bin/env python3
import sys

# Verificar se há parâmetros
if len(sys.argv) == 1:
    print("none")
else:
    # Iterar sobre cada parâmetro
    for arg in sys.argv[1:]:
        match arg:
            case param if param.endswith("ism"):
                continue  # Ignorar se já termina com "ism"
            case param:
                print(f"{param}ism")
