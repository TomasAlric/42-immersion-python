#!/usr/bin/env python3
import sys

# Verificar o número de parâmetros passados
if len(sys.argv) != 2:
    print("none")
else:
    # Solicitar ao usuário que insira uma palavra
    word = input("What was the parameter? ")

    # Verificar se a palavra inserida corresponde ao parâmetro passado
    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
