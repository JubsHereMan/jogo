import os
from personagens import jubs,seth,low

personagem_escolhido_nome = None

##menu
def limpar_tela():
    """Limpa a tela do console dependendo do sistema operacional."""
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux, macOS, etc.)
        os.system('clear')
def escolha_personagem(escolha):
    global personagem_escolhido_nome
    limpar_tela()
    if escolha == 1:
        print(jubs)
        print('\nJubs é um mago que possui a energia do Negativo, uma energia temporal que o permite aplicar dano temporal em seus inimigos'
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
        print('Seth é um grande velocista que consegue atingir a velocidade de Mark 1, ele possui a habilidade de atacar 2 vezes no mesmo turno '
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
        print('Low é um Spider, alguém com grande agilidade e capaz de se esquivar dos ataques dos seus inimigos, com suas teias ele também consegue dar stun em seus inimigos.')
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
def menu():
    limpar_tela()
    print('\nPara ver as informações do personagem, digite o seu respectivo número'
          '\n1. Jubs'
          '\n2. Seth'
          '\n3. Low')
    escolha = int(input('Digite a sua escolha: \n'))
    escolha_personagem(escolha)
def iniciar_jogo():
    limpar_tela()
    print('Bem-vindo ao seletor de personagens!')
    iniciar = int(input('Digite 1 para podermos começar: \n'))
    if iniciar == 1:
        menu()
    else:
        print('Opção inválida.')
#fim menu

#personagem

#Jubs
def curaTemporal(jubs):
    if jubs['tipo de energia']=='Negativo' and jubs['mana'] > 30:
        jubs['vida']+=6
        jubs['mana']-=30
        print('Jubs: O TEMPO CURA TODAS AS FERIDAS!!')
        print(f'{jubs['nome']}foi curado.A sua vida atual é:{jubs['vida']}')
        print(f'Jubs agora esta com {jubs['mana']} de mana')

    else:
        print(f'{jubs['nome']} não pode usar a habilidade de cura temporal.')


def Denyto(jubs):
    if jubs['tipo de energia']=='Negativo' and jubs ['mana']> 30:


iniciar_jogo()

limpar_tela()
if personagem_escolhido_nome:

    print('\nEm uma floresta sombria um herói chega. Aquele que nos salvará da perdição trazida pelo grande rei demônio.'
          f'\n{personagem_escolhido_nome} esta aqui para salvar o dia!' )
else:
    print('Nenhum personagem foi escolhido.')



