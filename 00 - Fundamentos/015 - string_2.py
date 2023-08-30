nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

# old style - não recomendado o uso, oriundo do python2
# delimitado por percentual  do tipo de dado, s = string, d= double
print("Nome: %s Idade: %d" % (nome, idade))

# delimitado pelo método format e pela sequência de variáveis especificadas
print("Nome: {} Idade: {}".format(nome, idade))

# aqui é possível delimitar a posição da variável começando com 0
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# aqui passamos variáveis aos atributos utilizados na string.
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(
    age=idade, name=nome))
# aqui já passamos os dados formatados em um objeto
print("Nome: {nome} Idade: {idade}".format(**dados))

# aqui é o método mais recomendado.
print(f"Nome: {nome} Idade: {idade}")
# impressão com formatação do resultado em número de casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
