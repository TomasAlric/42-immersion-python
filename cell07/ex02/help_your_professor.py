#!/usr/bin/env python3

def average(students_scores):
    # Calculando a soma das notas e a quantidade de alunos
    total_scores = sum(students_scores.values())
    num_students = len(students_scores)
    # Calculando a média
    return total_scores / num_students

# Dicionário representando a classe 3B
class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

# Dicionário representando a classe 3C
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

# Imprimindo a média de cada classe
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
