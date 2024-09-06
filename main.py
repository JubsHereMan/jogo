import os
from time import sleep
from personagens import jubs, seth, low
from inimigosFloresta import *

inimigos=[inimigosFloresta]
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

personagem_escolhido_nome = None

# Função de level up e habilidades
def levelUp(personagem_escolhido):
    if personagem_escolhido['inimigos mortos'] >= 4:
        personagem_escolhido['nivel'] += 1
        print(f"{personagem_escolhido['nome']} subiu para o nível {personagem_escolhido['nivel']}!")

        if personagem_escolhido['classe'] == 'mago':
            ganhoHabilidadesMago(personagem_escolhido)
        else:
            print(f"Classe desconhecida para {personagem_escolhido['nome']}.")
    else:
        print(
            f"{personagem_escolhido['nome']} ainda não pode subir de nível. Derrote mais {4 - personagem_escolhido['inimigos mortos']} inimigos.")


def ganhoHabilidadesMago(personagem_escolhido):
    if personagem_escolhido['nivel'] == 2:
        print(f"{personagem_escolhido['nome']} subiu para o nível 2!")
        print(
            'O tempo fala com Jubs, o molda... o fortalece... agora com maior compreensão sobre o tempo Jubs subiu de nivel.'
            f'\ndano= {personagem_escolhido["dano"] - 2} => {personagem_escolhido["dano"]}'
            f'\nmana= {personagem_escolhido["mana"] - 20} => {personagem_escolhido["mana"]}'
            f'\nvida= {personagem_escolhido["vida"] - 5} => {personagem_escolhido["vida"]}'
        )
    elif personagem_escolhido['nivel'] == 3:
        print(f"{personagem_escolhido['nome']} subiu para o nível 3!")
        print(
            'O tempo fala com Jubs, o molda... o fortalece... agora com maior compreensão sobre o tempo Jubs subiu de nivel.'
            f'\ndano= {personagem_escolhido["dano"] - 2} => {personagem_escolhido["dano"]}'
            f'\nmana= {personagem_escolhido["mana"] - 20} => {personagem_escolhido["mana"]}'
            f'\nvida= {personagem_escolhido["vida"] - 5} => {personagem_escolhido["vida"]}'
        )
    elif personagem_escolhido['nivel'] == 4:
        print(f"{personagem_escolhido['nome']} subiu para o nível 4!")
        print(
            'O tempo fala com Jubs, o molda... o fortalece... agora com maior compreensão sobre o tempo Jubs subiu de nivel.'
            f'\ndano= {personagem_escolhido["dano"] - 2} => {personagem_escolhido["dano"]}'
            f'\nmana= {personagem_escolhido["mana"] - 20} => {personagem_escolhido["mana"]}'
            f'\nvida= {personagem_escolhido["vida"] - 5} => {personagem_escolhido["vida"]}'
        )


# Jubs
def curaTemporal(jubs):
    if jubs['tipo de energia'] == 'Negativo' and jubs['mana'] > 30:
        jubs['vida'] += 6
        jubs['mana'] -= 30
        print('Jubs: O TEMPO CURA TODAS AS FERIDAS!!')
        print(f'{jubs["nome"]} foi curado. A sua vida atual é: {jubs["vida"]}')
        print(f'Jubs agora está com {jubs["mana"]} de mana')
    else:
        print(f'{jubs["nome"]} não pode usar a habilidade de cura temporal.')






iniciar_jogo()

limpar_tela()
if personagem_escolhido_nome:
    print(
        '\nEm uma floresta sombria um herói chega. Aquele que nos salvará da perdição trazida pelo grande rei demônio.'
        f'\n{personagem_escolhido_nome} está aqui para salvar o dia!\n')

sleep(1.0)
print('CAPITULO | \nA GRANDE FLORESTA\n')


sleep(1.5)
entrarFloresta=int(input(f'\n{personagem_escolhido_nome} ao chegar na floresta você consegue perceber que coisas estão estranhas,'
                     f'uma grande massa roxa e pulsante esta cobrindo as arvores.\n Você sente repulsa em apenas ter ideia de entrar na grande floresta '
                     f'\no que você ira fazer?'
                     f'\n1. Entrar na floresta'
                     f'\n2. Deixar a aventura de lado e voltar para a segurança de casa \n'))

while entrarFloresta != 1 and 2:
    print('Escolha uma upção valida!!\n')
    entrarFloresta=int(input(f'\n{personagem_escolhido_nome} ao chegar na floresta você consegue perceber que coisas estão estranhas,'
                     f'uma grande massa roxa e pulsante esta cobrindo as arvores.\n Você sente repulsa em apenas ter ideia de entrar na grande floresta '
                     f'\no que você ira fazer?'
                     f'\n1. Entrar na floresta'
                     f'\n2. Deixar a aventura de lado e voltar para a segurança de casa \n'))
match entrarFloresta:
    case 1:
        print('\nAo entrar na floresta um odor indescritivel invade as suas narinas '
            '\nao olhar para os lados você se depara com marcas de garras que estão com esse mesmo residuo das arvores'
            '\n você não está sozinho... agora não ha mais volta... lembre-se disso.')
    case 2:
        print('\nAo voltar para sua casa, você consegue acompanhar com os proprios olhos enquanto o grande rei demonio espalha alguma coisa'
            '\n sobre os 4 ventos que esta infectando tudo e todos... uma doença lastimavel que infecta e faz com que as pessoas não sejam'
            '\n mais donas dos seus proprios corpos... vocÊ perdeu a chance de fazer a diferença...\n')
        
        voltarMenu= 0
        while voltarMenu != 1: 
            voltarMenu= int(input('\ndigite 1 para voltar ao menu'))
        iniciar_jogo()

      
    case _:
        print('\nescolha uma opção valida!')
        entrarFloresta

escolhaCaminho1= int(input(f"logo de cara {personagem_escolhido_nome} consegue perceber dois caminhos distintos... qual vai ser a sua escolha?
            \n 1. O caminho cheio das massas roxas
            \n 2. O caminho com menos massas roxas"))

    case 1:
        print(f'''
    \ncaminhando cada vez mais fundo na floresta {personagem_escolhido_nome} se depara mais ainda com essa massa roxa, agora cada vez mais presente no local...
é dificil de respirar... com um olhar atento percebe-se que essa massa roxa esta soltando esporos...
talvez não seja uma boa ideia avançar sem algo para se proteger...''')
    case _:
        print('')
    
