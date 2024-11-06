#!/usr/bin/env python3

# Define o array original de números
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Cria o novo array adicionando 2 a cada valor do array original
new_array = [x + 2 for x in original_array]

# Exibe ambos os arrays
print(f"Original array: {original_array}")
print(f"New array: {new_array}")
