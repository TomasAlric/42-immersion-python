#!/usr/bin/env python3
import sys
import re

# Verifica se o número de parâmetros é exatamente 2
if len(sys.argv) == 3:
    # A palavra-chave e a string de busca
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    # Usa re.findall para encontrar todas as ocorrências da palavra-chave
    matches = re.findall(r'\b' + re.escape(keyword) + r'\b', search_string)

    # Exibe o número de ocorrências, ou "none" se não houver nenhuma
    print(len(matches) if matches else "none")
else:
    # Se o número de parâmetros for diferente de 2, exibe "none"
    print("none")
