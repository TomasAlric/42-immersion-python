#!/usr/bin/env python3

# Definindo a função find_the_redheads
def find_the_redheads(family_members):
    # Usando filter para obter as chaves onde o valor é 'red'
    redheads = list(filter(lambda name: family_members[name] == 'red', family_members.keys()))
    return redheads

# Exemplo de dicionário representando a família
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Imprimindo o resultado da função
print(find_the_redheads(dupont_family))
