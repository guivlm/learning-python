nome = "gUIlherME"

print(nome.upper())  # maiscula
print(nome.lower())  # minuscula
print(nome.title())  # primeira maisucula

texto = "  Olá mundo!    "

print(texto + ".")  # concatena ponto no final
print(texto.strip() + ".")  # remove espaços de ambos os lados
print(texto.rstrip() + ".")  # remove espaços da direita
print(texto.lstrip() + ".")  # remove espaços da esquerda

menu = "Python"

print("####" + menu + "####")  # concatenação regular
# coloca string no centro concatenado com 14 espaços (7 de cada lado)
print(menu.center(14))
# coloca string no centro concatenado com 14 símbolos definidos (7 de cada lado)
print(menu.center(14, "#"))
print("-".join(menu))  # separa string com sequência de caracteres entre letras
