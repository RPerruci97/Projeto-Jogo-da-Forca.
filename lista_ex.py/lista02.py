#Lista-estruturas de decisão

#1
num = float(input("Digite um valor inteiro ou real:")) 
if num > 10:
    print("O número digitado é MAIOR que 10.")
else: 
    print("O número digitado é MENOR que 10.") 

#2
num = float(input("Digite um valor numérico:")) 
if num >= 0:
    print("O valor é positivo.") 
else:
    print("O valor é negativo.") 
    
#3
maca = int(input("Digite quantas maçãs você deseja comprar:")) 
if maca < 12:
    print(f"Você comprou menos de uma duzia portanto o valor pago será {(maca * 1.30)} reais.") 
else:
    print(f"Você comprou mais de uma duzia portanto o valor pago será {(maca * 1.00)} reais.")  

#4 
nota1 = float(input("Digite sua primeira nota:")) 
nota2 = float(input("Digite sua segunda nota:")) 
media = ((nota1+nota2)/2) 
if media >= 6:
    print(f"Parabéns! Sua média foi {media}, você foi aprovado.") 
else: 
    print(f"Sua média foi{media}, ifelizmente não conseguiu.") 

#5
val1 = float(input("Digite o primeiro valor")) 
val2 = float(input("Digite o segundo valor")) 
if val1 > val2:
    print(f"O maior valor digitado foi:{val1}.") 
else: 
    print(f"O maior valor digitado foi:{val2}") 

#6
val1 = float(input("Digite o primeiro valor:")) 
val2 = float(input("Digite o segundo valor:")) 
if val1 > val2:
    print(val1, val2) 
else: 
    print(val2, val1)

#7 
conta = int(input("Digite o número da sua conta:")) 
saldo = float(input("Digite o valor do seu saldo:"))
debito = float(input("Digite o valor do seu debito:")) 
credito = float(input("Digite o valor do seu crédito:"))
atual = saldo - (debito + credito) 
print(f"Seu saldo atual é de {atual} reais.") 
if atual > 0:
    print("Seu saldo é positivo.") 
else:
    print("Seu saldo é negativo.") 

#8 
estoque = int(input("Digite o valor da quantidade atual de estoque:")) 
min = int(input("Digite o valor da quantidade mínima de estoque:")) 
max = int(input("Digite o valor da quantidade máxima de estoque:")) 
media = ((max + min)/2) 
print(f"A quantidade média que se deve ter em estoque é {media}.")
if estoque >= media:
    print("Efetuar compra.") 
else: 
    print("Não efetuar compra.") 


#9 
nota1 = float(input("Digite sua primeira nota:")) 
nota2 = float(input("Digite sua segunda nota:")) 
media = ((nota1+nota2)/2) 
if media >= 9:
    print("A") 
elif media < 9 and media >= 7.5:
    print("B") 
elif media < 7.5 and media >=6:
    print("C") 
elif media < 6 and media > 4 :
    print("D") 
else:
    print("E") 
print(f"Sua média é {media}.")
lista = ["A","B","C"]
if media >= 6: 
    print("Aprovado!")
else:
    print("Reprovado!")

