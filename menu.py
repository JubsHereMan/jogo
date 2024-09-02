import os
from personagens import *

##menu



def limpar_tela():
    """Limpa a tela do console dependendo do sistema operacional."""
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux, macOS, etc.)
        os.system('clear')


def iniciar_jogo():
    limpar_tela()
    print('Bem-vindo ao seletor de personagens!')
    iniciar = int(input('Digite 1 para podermos começar: \n'))
    if iniciar == 1:
        menu()
    else:
        print('Opção inválida.')


def menu():
    limpar_tela()
    print('\nPara ver as informações do personagem, digite o seu respectivo número'
          '\n1. Jubs'
          '\n2. Seth'
          '\n3. Low')
    escolha = int(input('Digite a sua escolha: \n'))
    escolha_personagem(escolha)


def escolha_personagem(escolha):
    global personagem_escolhido_nome
    limpar_tela()
    if escolha == 1:
        print(jubs)
        print(
            '\nJubs é um mago que possui a energia do Negativo, uma energia temporal que o permite aplicar dano temporal em seus inimigos'
            '\n e também curar os seus aliados ou a si mesmo voltando suas feridas no tempo')
        confirmacao = input('Este é o personagem que você quer jogar?'
                            '\n1. Sim'
                            '\n2. Não\n')
        if confirmacao == '2':
            print('Tudo bem, vamos para o menu para você poder escolher outro:')
            menu()
        elif confirmacao == '1':
            personagem_escolhido_nome = jubs['nome']
            print(f'Ótima escolha! Você escolheu {personagem_escolhido_nome}.')
        else:
            print('Opção inválida. Retornando ao menu.')
            menu()

    elif escolha == 2:
        print(seth)
        print(
            'Seth é um grande velocista que consegue atingir a velocidade de Mark 1, ele possui a habilidade de atacar 2 vezes no mesmo turno '
            'devido a sua grande velocidade.')
        confirmacao = input('Este é o personagem que você quer jogar?'
                            '\n1. Sim'
                            '\n2. Não\n')
        if confirmacao == '2':
            print('Tudo bem, vamos para o menu para você poder escolher outro:')
            menu()
        elif confirmacao == '1':
            personagem_escolhido_nome = seth['nome']
            print(f'Ótima escolha! Você escolheu {personagem_escolhido_nome}.')
        else:
            print('Opção inválida. Retornando ao menu.')
            menu()
    elif escolha == 3:
        print(low)
        print(
            'Low é um Spider, alguém com grande agilidade e capaz de se esquivar dos ataques dos seus inimigos, com suas teias ele também consegue dar stun em seus inimigos.')
        confirmacao = input('Este é o personagem que você quer jogar?'
                            '\n1. Sim'
                            '\n2. Não\n')
        if confirmacao == '2':
            print('Tudo bem, vamos para o menu para você poder escolher outro:')
            menu()
        elif confirmacao == '1':
            personagem_escolhido_nome = low['nome']
            print(f'Ótima escolha! Você escolheu {personagem_escolhido_nome}.')
        else:
            print('Opção inválida. Retornando ao menu.')
            menu()
    else:
        print('Escolha de personagem inválida.')
        menu()
