#!/usr/bin/env python3

def shrink(s):
    # Exibe os primeiros 8 caracteres da string
    print(s[:8])

def enlarge(s):
    # Se a string tem menos de 8 caracteres, adiciona 'Z' até completar 8
    print(s.ljust(8, 'Z'))

# Verifica se existem parâmetros passados para o programa
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)  # Se a string for maior que 8, chama shrink
        else:
            enlarge(param)  # Se a string for menor ou igual a 8, chama enlarge
