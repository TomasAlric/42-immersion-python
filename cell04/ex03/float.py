#!/usr/bin/env python3

# Solicitar o número ao usuário
number = float(input("Give me a number: "))

# Verificar se o número é inteiro ou decimal
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
