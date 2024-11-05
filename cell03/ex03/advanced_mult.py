#!/usr/bin/env python3

# Inicializando a variável que controla as tabelas
i = 0

# Loop externo para controlar cada tabela de multiplicação (de 0 a 10)
while i <= 10:
    print(f"Table de {i}: ", end="")

    # Inicializando o multiplicador
    j = 0

    # Loop interno para calcular e exibir os múltiplos (de 0 a 10)
    while j <= 10:
        print(f"{i * j} ", end="")
        j += 1  # Incrementando o multiplicador

    print()  # Nova linha após cada tabela
    i += 1  # Incrementando a tabela atual
