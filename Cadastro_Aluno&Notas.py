# Sistema de Cadastro de Aluno e Notas
alunos = []
notas = []


print("--- CADASTRO DE ALUNOS E NOTAS RESPECTIVAS ---")
qtd_de_alunos = int(input("Quantos alunos quer cadastrar ?"))

for i in range(qtd_de_alunos):
  nome = input(f"Digite o nome do {i+1}º aluno: ")
  alunos.append(nome)
  
  notas_do_aluno = []
  for j in range(3):
    valor = float(input(f"Digite a {j+1}ª nota do {nome}: "))
    notas_do_aluno.append(valor)
  notas.append(notas_do_aluno)

classe = dict(zip(alunos, notas))

print(f"{qtd_de_alunos} ALUNO(S) CADASTRADOS !")

# Calculando a média e seprando aprovados/reprovadoss
aprovados= {}
reprovados = {}

for nome, lista_de_notas in classe.items():
  media = sum(lista_de_notas) / len(lista_de_notas)
  if media >= 7:
    aprovados[nome] = media
  else:
    reprovados[nome] = media  


print("\nAlunos Aprovados:")
for nome, media in aprovados.items():
  print(f"{nome}: média: {media:.2f}!")   

print("\nAlunos Reprovados:") 
for nome, media in reprovados.items():
  print(f"{nome}: média: {media:.2f}!")