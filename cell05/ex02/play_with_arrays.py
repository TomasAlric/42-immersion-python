#!/usr/bin/env python3

# Define o array original de números
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Filtra os valores maiores que 5 e cria o novo array com 2 adicionado a cada valor
new_array = [x + 2 for x in original_array if x > 5]

# Exibe os dois arrays
print(original_array)
print(new_array)
