import random
import os

plHp = 10
plMaxHp = 10
plAttack = 2
plDefense = 1

enemyHp = 8
enemyMaxHp = 8
enemyAttack = 1
enemyDefense = 0

contadorTurno = 0
lista = ['ataque','item','magia','correr'] 

def roll():
    d6 = random.randint(1,6)
    return d6

def dano(turn,Ataque):
    rolagem = roll()
    if turn == 0:
        jogadorDano = Ataque+rolagem
        return jogadorDano
    else:
        inimigoDano = Ataque+rolagem
        return inimigoDano


while True:
    if plHp <= 0 or enemyHp <= 0:
        print('Fim de jogo')
        break
    
    else:
        turno = contadorTurno%2
        print('\n','vida do jogador:',plHp,'/',plMaxHp,'\n')
        print('\n','Vida do inimigo',enemyHp,'/',enemyMaxHp,'\n')


        if turno == 0: #turno do jogador
            print('Vez do jogador')
            print(lista)
            escolha = input('Escolha uma ação: ')

            if escolha.lower() in lista:

                if escolha.lower() == 'ataque':
                    danoCausado = dano(turno,plAttack)
                    print('Inimigo recebeu', danoCausado,'de dano')
                    enemyHp -= danoCausado-plDefense
                    contadorTurno+=1

                elif escolha.lower() == 'item':
                    print('item ainda não disponivel')

                elif escolha.lower() == 'magia':
                    print('magia ainda não disponivel')

                else:
                    run = roll()
                    if run%2 == 0:
                        print('Escapou!')
                        break
                    else:
                        print('Não conseguiu fugir')
                        contadorTurno+=1
                        
            else:
                print('escolha invalida')

        else: #Vez do inimigo
            print('Vez do inimigo')
            danoCausado = dano(turno,enemyAttack)
            print('inimigo causou',danoCausado,'de dano') 
            plHp -= danoCausado
            contadorTurno+=1



    
    os.system('pause')

    if contadorTurno > 10:
        break
    
    
