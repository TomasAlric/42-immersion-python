#!/usr/bin/env python3

def famous_births(people):
    # Ordenando o dicionário pelas datas de nascimento
    sorted_people = sorted(people.items(), key=lambda x: x[1]['date_of_birth'])

    # Exibindo os resultados
    for person in sorted_people:
        name = person[1]['name']
        birth_date = person[1]['date_of_birth']
        print(f"{name} is a great scientist born in {birth_date}.")


# Dicionário de mulheres cientistas com seus nomes e datas de nascimento
women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

# Chamando a função famous_births
famous_births(women_scientists)
