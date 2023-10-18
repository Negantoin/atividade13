# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O primeiro número (", num1, ") é o maior dos três")
elif num2 > num1 and num2 > num3:
    print("O segundo número (", num2, ") é o maior dos três")
elif num3 > num1 and num3 > num2:
    print("O terceiro número (", num3, ") é o maior dos três")