#Esta primeira lista de exercícios é sobre estrutura sequencial 
#Faça um programa que converta metros para centímetros 

print("Vamos converter metros para centímetros")
num = float(input("Digite um valor em metros:")) 
con = num * 100  
print(f"O valor em metros digitado foi {num}m, convertendo fica {con}cm.") 

#Faça um programa que pergunte o raio de um círculo, 
#calcule e mostre a sua área 

import math 
raio = float(input("Digite o valor do raio de um círculo:")) 
area = math.pi * raio**2 
print(f"A área do círculo é {area:.2f}.") 

#Faça um programa que calcule a área de um quadrado 
#em seguida mostre o dobro dessa área para o usuário 

lado = float(input("Digite a medida do lado de um quadrado:")) 
area = lado**2  
print(f"O lado do seu quadrado mede {lado}, portanto sua área é {area}.") 

#Faça um programa que pergunte quanto você ganha por hora e quantas
#horas você trabalha no mês, calcule e mostre seu salário final 

valor = int(input("Digite o valor da sua hora trabalhada:")) 
hora = int(input("Quantas horas você trabalha no mês?")) 
total = valor*hora 
print(f"O valor do seu salário total no mês é de {total} reais.") 

#Faça um programa que peça a tem peratura em graus F° e converta em C° 

print("Vamos converter a temperatura de C° para F°!") 
f = int(input("Digite a temperatura em F°:")) 
c = 5 * ((f-32)/9) 
print(f"A temperatura atual em F° é {f} sua conversão para C° fica {c:.2f}") 

#Faça um programa que peça a tem peratura em graus C° e converta em F° 

print("Vamos converter a temperatura de C° para F°")
c = float(input("Digite a temperatura em C°:"))
f = ((9*c)/5) + 32
print("A temperatura atual é {} C° e convertendo fica {} F°.".format(c,f)) 
 
 #Faça uma sequencia de estruturas matemáricas
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))
num3 =  float(input("Digite um número real:")) 
print(f"O produto do dobro do primeiro mais metade so segundo é {(num1*2)+(num2/2)}") 
print(f"A soma do triplo do primeiro com o terceiro é {(num1*3)+(num3)}") 
print(f"O terceiro número elevado ao cubo é {(num3**3)}") 

#Calcule o peso ideal de uma pessoa

altura = float(input("Digite sua altura:")) 
peso_ideal = (72.7 * altura)-58 
print(f"O peso ideal para você equivalente a sua altura é {peso_ideal}kg.") 

#Calcule o peso ideal um homem e uma mulher

altura = float(input("Digite sua altura:")) 
print(f"O peso ideal para um homem equivalente a sua altura é {((72.7 * altura)-58):.2f}kg.")  
print(f"O peso ideal para uma mulher equivalente a sua altura é {((62.1 * altura)-44.7):.2f}kg.") 
