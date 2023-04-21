import os
os.system('cls')

#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint #Biblioteca para randomizar numeros
from time import sleep #Biblioteca para dar uns segundos a cada ação 

itens = ('Pedra 🪨', 'Papel 🗒️', 'Tesoura ✂️')
computador = randint (0, 2) #está sorteando os numeros da variavel itens
print('JOKENPÔ BOLADO')
jogador = int(input('''Sua jogada:
[0] Pedra 🪨
[1] Papel 🗒️
[2] Tesoura ✂️
Qual você escolhe? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *10)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' *10)
if computador == 0:
    if jogador == 0:
         print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')