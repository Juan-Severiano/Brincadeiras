from random import randint
from time import sleep
l = """
[1] Pedra
[2] Papel
[3] Tesoura
[4] Lagarto
[5] Spok
"""
d = {
    
1:'Pedra',
2:'Papel',
3:'Tesoura',
4:'Lagarto',
5:'Spok'


}
regras = """
something
"""


j = input('Voce quer jogar? S/N\n')
if (j == 's') or (j == 'sim'):
    i = input('Você ja sabe as regras do jogo? S/N')
    if i == 'S':

        while True:
            print('Suas opcoes sao:\n{}'.format(l))
            r = int(input('Qual opcao voce deseja? '))
            sleep(3)
            c = randint(1, 5)
            if r == c:
                print(f'Você escolheu {d[r]} e o computador tambem escolheu {d[c]}')
                print('EMPATE')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 1) and (c == 2):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ PERDEU\nPapel sufoca a Pedra')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 1) and (c == 3):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nPedra esmaga Tesoura')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 1) and (c == 4):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nPedra esmaga Lagarto')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 1) and (c == 5):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('EMPATE\nSpok valoriza a Pedra, todo o mundo sai ganhando')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)

            elif (r == 2) and (c == 3):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('O Computador VENCEU\nTesoura corta papel')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 2) and (c == 4):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('O Computador VENCEU\nLagarto come Papel')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 2) and (c == 5):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nPapel refuta Spock')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 2) and (c == 1):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nPapel cobre a Pedra')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)

            elif (r == 3) and (c == 1):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nPedra amassa Tesoura')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 3) and (c == 2):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nTesoura corta Papel')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 3) and (c == 4):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nTesoura decapta Lagarto')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 3) and (c == 5):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('O Computador VENCEU\nSpock quebra a Tesoura')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)

            elif (r == 4) and (c == 1):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ PERDEU\nPedra esmaga Lagarto')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 4) and (c == 2):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nLagarto come Papel')
                sleep(3)
            elif (r == 4) and (c == 3):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ PERDEU\nTesoura decapta Lagarto')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 4) and (c == 5):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nLagarto envenena Spock')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)

            elif (r == 5) and (c == 1):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('EMPATE\nSpock valoriza a Pedra, todos saem ganhando')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 5) and (c == 2):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCE PERDEU\nPapel refuta Spock')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 5) and (c == 3):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ VENCEU\nSpock quebra a Tesoura')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            elif (r == 5) and (c == 4):
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                print('VOCÊ PERDEU\nLagarto envenena Spock')
                p = input('Você quer continuar? S/N ')
                if p == 'N':
                    break
                sleep(3)
            
    elif i == 'N':
        print(regras)
    else:
        print('Digite um valor valido')
        

elif (j == 'n') or (j == 'nao') or (j == 'não'):
    print('pois valeu ai menó, volte sempre')

else:
    print('digite um valor válido')
    

