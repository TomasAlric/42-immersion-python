#!/usr/bin/env python3

while True:
    # Solicita ao usuário uma entrada
    user_input = input("What you gotta say? : ")

    # Verifica se a entrada é exatamente "STOP"
    if user_input.strip() == "STOP":
        break  # Sai do loop

    # Exibe uma mensagem confirmando a entrada do usuário
    print(f"I got that! Anything else? : {user_input}")
