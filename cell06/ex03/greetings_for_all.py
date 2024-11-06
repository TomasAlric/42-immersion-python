#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')  # Deve exibir: Hello, Alexandra.
greetings('Wil')        # Deve exibir: Hello, Wil.
greetings()             # Deve exibir: Hello, noble stranger.
greetings(42)           # Deve exibir: Error! It was not a name.
