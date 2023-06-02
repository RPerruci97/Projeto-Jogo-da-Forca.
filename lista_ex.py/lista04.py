#Desenvolva os algoritmos abaixo em linguagem Python. Utilize o VS Code ou Pycharm, mas ao
#final entregue ao professor um arquivo .py para cada questão desenvolvida. - Lista de estrutura de dados

#1  
pessoa = {} 
pessoa["primeiro_nome"] = "Rafaela" 
pessoa["sobrenome"] = "Perruci" 
pessoa["idade"] = 26 
pessoa["cidade"] = "João Pessoa" 
print(f"A {pessoa['primeiro_nome']} {pessoa['sobrenome']}, tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")  

#2------------------------------------------------------------------------------------  
num_preferido = {"Rafaela": 8, "Carol": 6, "Leo": 7, "Victor": 9, "Maisa": 5} 
for k, v in num_preferido.items():
    print(f"O(a) {k}, tem como número preferido {v}.")

#3---------------------------------------------------------------------
estudantes = [] 
for c in range(10):
    aluno = {}
    nome = str(input("Digite o seu nome:")).strip() 
    aluno["nomes"] = nome 
    
    notas = []
    for i in range(4):
        nota = float(input("Digite sua nota:")) 
        notas.append(nota) 

    medias = sum(notas) / 4
    aluno["notas"] = notas
    aluno["media"] = medias 
    estudantes.append(aluno)
contador = 0
for aluno in estudantes:
    if aluno["media"] >= 7:
        contador += 1  
print(f"O número de alunos com média maior ou igual a 7 é {contador}") 
print(estudantes) 

#----------outra forma de representar a questão 3-----------------------
from random import randint 
medias = []  
todas_as_notas = []
cont = 0
for c in range(10):
    notas = []
    for i in range(4):
        nota = randint(1, 10)
        notas.append(nota)
        todas_as_notas.append(notas) 

    media = sum(notas)/4 
    medias.append(media) 
            
    if media >= 7:
        cont += 1 
print(f"Existem {cont} alunos com média maior ou igual a 7.") 
print(todas_as_notas) 
print(medias)

#4------------------------------------------------------------------------------------------------ 
idades = [18, 16, 15, 15, 25, 5, 15, 9, 9, 8, 8, 9, 11, 11, 13, 13, 17, 
          9, 7, 13, 14, 16, 16, 8, 9, 10, 10, 13, 14, 15] 

alturas = [158, 170, 158, 180, 180, 145, 145, 175, 175, 140, 130, 140, 130,
           155, 155, 154, 160, 180, 135, 150, 175, 160, 168, 165, 170, 120, 160, 165, 145, 140] 

media_altura = sum(alturas)/30 

contador = 0
for c in range(0, len(idades)):
    if idades[c] > 13 and alturas[c] < media_altura:
        contador += 1 

print(f"A quantidade de alunos com mais de 13 anos inferior a altura média são {contador}.") 

#5-------------------------------------------------------------------------------------------
numeros = []
for c in range(5):
    num = int(input("Digite um número inteiro:"))
    numeros.append(num) 
print(numeros)
