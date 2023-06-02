#Lista de exercícios - Estrutura de repetição
#1 Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
#divididos por 11, produzam o resto igual a 5.
for num in range (1000, 2001): 
    if num % 11 == 5:
        print(num) 
# outra forma da mesma estrututa de looping-------------------- 
for num in range (1000, 2001): 
    while num % 11 == 5:
        print(num) 
        num+=1
        break

#2 Faça um programa que mostre as tabuadas dos números de 1 a 10. 
for i in range(1, 11):
     for num in range(1, 11):
          res = i * num 
          print(f"{i} x {num} = {res}") 

#3 Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
#pessoa acessando cada elemento da lista um de cada vez. 
from time import sleep 
amigos = ["carol", "leticia", "renata", "leo", "victor"] 
for obj in amigos:
    print(obj)
    sleep(0.5) 
print("FIM") 

#4 Faça um programa que receba um número e que calcule e mostre a tabuada desse número.. 
num = int(input("Digite o número que você deseja tabular:"))  
for i in range(0, 11):
        res = num * i 
        print(f"{num} x {i} = {res}")    
#outras formas do mesmo exercício--------------------------------------------------
num = int(input("Digite o número que você deseja tabular:")) 
c = 1
while c <= 10:
    res = num * c 
    print(f"{num} x {c} = {res}")
    c += 1 
#--------------------------------------------------------------------------
while True:
    num = int(input("Quer descobrir a tabuada de qual valor?")) 
    if num < 0:
        break
    for c in range(0, 11):
        res = num * c 
        print(f"{num} x {c} = {res}.") 
print("Valor incorreto, tente novamente.")

#5 Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo. 
from time import sleep 
amigos = ["carol", "leticia", "renata", "leo", "victor"] 
for obj in amigos:
    print(f"Olá {obj}, como vai você?")
    sleep(0.5) 
print("FIM") 

#6 Seja criativo ao desenvolver este programa  
from time import sleep 
celeb = ["Rihanna", "Xuxa", "Djonga", "Neymar", "Donald Gloover"] 
for obj in celeb:
    print(f"Olá {obj}, você foi convidado para minha festa de aniversário! Aguardo sua presença lá.")
    sleep(1) 
print(f"{celeb[3]}, não poderá comparecer ao jantar,portanto, será substituído.")
del celeb[3] 
celeb.insert(3, "Ariana Grande") 
for obj in celeb:
    print(f"Olá {obj}, você foi convidado para minha festa de aniversário! Aguardo sua presença lá.")
    sleep(1)

#7 Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até
#agora 
cadastro = {}  
for i in range(1):
    nome = str(input("Digite seu nome completo:")) 
    idade = int(input("Digite sua idade:"))
    email = str(input("Digite seu email:")) 
    
    cadastro["nome"] = nome
    cadastro["idade"] = idade
    cadastro["email"] = email

print(f"O cadastro de {nome}, foi um sucesso!")
print(f"Aqui estão os seus dados completos: {cadastro}")



