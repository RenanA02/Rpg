#importação de bibliotecas
import random
import os

#declaração de variaveis
plHp = 10
plMaxHp = 10
plAttack = 2
plDefense = 1
pocaoDeVida = 2

enemyHp = 8
enemyMaxHp = 8
enemyAttack = 1
enemyDefense = 0

contadorTurno = 0
lista = ['ataque','item','magia','correr'] 


def roll(): #rolagem de 1d6
    d6 = random.randint(1,6)
    return d6

def dano(turn,Ataque): #calculo do dano se baseando no turno
    rolagem = roll()
    if turn == 0:
        jogadorDano = Ataque+rolagem
        return jogadorDano
    else:
        inimigoDano = Ataque+rolagem
        return inimigoDano

def inventario():
    itens = ['poção', 'bomba', 'espadão']
    print('   Equipamentos:\n')
    a = 0
    for i in itens:
        print ('x',itens[a])
        a += 1
    #print(f'1x {itens[0]} - Recupera 2 de vida\n')
    selecao = input('Escola o item a ser usado, ou digite "sair": ')
    if selecao == 'sair':
        os.system('cls')
        pass
    elif selecao.lower() in itens:
        if selecao == 'poção':
            os.system('cls')
            return ('poção')
        
        elif selecao == 'bomba':
            pass
        
        elif selecao == 'espadão':
            pass
    else:
        print(f'{selecao.capitalize()} não é um item valido')
        os.system('pause')
        os.system('cls')






while True:

    if plHp <= 0: #verifica se o jogador ou o inimigo ainda estão vivos
        print('Fim de jogo\nVocê morreu')
        break
    elif enemyHp <= 0:
        print('Fim de jogo, Imigigo derrotado')
        break
    
    else:
        turno = contadorTurno%2
        print(f'\nVida do jogador: {plHp}/{plMaxHp}\n')
        print(f'\nVida do Inimigo: {enemyHp}/{enemyMaxHp}\n')


        if turno == 0: #turno do jogador
            print('Vez do jogador')
            print(lista)
            escolha = input('Escolha uma ação: ')

            if escolha.lower() in lista:
                os.system('cls')
                if escolha.lower() == 'ataque':
                    danoCausado = dano(turno,plAttack)
                    print('Inimigo recebeu', danoCausado,'de dano')
                    enemyHp -= danoCausado
                    contadorTurno+=1
                    os.system('pause')

                elif escolha.lower() == 'item':
                    item = inventario()
                    if item == 'poção':
                        print('Poção foi usada')
                        plHp += 2
                        contadorTurno += 1
                        if plHp > plMaxHp:
                            plhp = plMaxHp



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
                        os.system('pause')

            else:
                print('escolha invalida')

        else: #Vez do inimigo
            print('Vez do inimigo')
            os.system('pause')
            os.system('cls')
            danoCausado = dano(turno,enemyAttack)
            print('inimigo causou',danoCausado,'de dano') 
            plHp -= danoCausado
            contadorTurno+=1
            os.system('pause')
            os.system('cls')

    if contadorTurno > 10:
        break
    
    
'''Pesquisar sobre pygame
fazer inventario
fazer menu
fazer mais inimigos
fazer magias
fazer itens
fazer moedas/lojas
fazer xp e lvl up'''