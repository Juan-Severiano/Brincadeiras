from time import sleep
from random import randint

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
Pedra Papel Tesoura Lagarto Spock foi criado por Sam Kass
como uma forma de melhoria do jogo original Pedra papel tesoura

Vida longa a Sam Kass

REGRAS:
A tesoura corta o papel
O papel cobre a Pedra
A pedra esmaga o lagarto
O lagarto envenena o Spock
O spock quebra a tesoura
A tesoura decapta o lagarto
O lagarto come o papel
O papel refuta o Spock
O Spock valoriza a pedra
E a pedra amassa a tesoura

"""

while True:
    j = input('Voce quer jogar? S/N\n')
    if j == 's':
        i = input('Você ja sabe as regras do jogo? S/N')
        if (i == 'S') or (i == 'sim'):
        
            while True:
                print('Suas opcoes sao:\n{}'.format(l))
                r = int(input('Qual opcao voce deseja? '))
                sleep(3)
                c = randint(1, 5)
                print(f"Voce escolheu {d[r]} e o OCmputador escolheu {d[c]}")
                if r == c:
                    print('EMPATE')
                    
                elif (r == 1) and (c == 2):
                    print('VOCÊ PERDEU\nPapel sufoca a Pedra')
                    
                elif (r == 1) and (c == 3):
                    print('VOCÊ VENCEU\nPedra esmaga Tesoura')
                    
                elif (r == 1) and (c == 4):
                    print('VOCÊ VENCEU\nPedra esmaga Lagarto')
                    
                elif (r == 1) and (c == 5):
                    print('EMPATE\nSpok valoriza a Pedra, todo o mundo sai ganhando')
                    
    
                elif (r == 2) and (c == 3):
                    print('O Computador VENCEU\nTesoura corta papel')
                    
                elif (r == 2) and (c == 4):
                    print('O Computador VENCEU\nLagarto come Papel')
                    
                elif (r == 2) and (c == 5):
                    print('VOCÊ VENCEU\nPapel refuta Spock')
                    
                elif (r == 2) and (c == 1):
                    print('VOCÊ VENCEU\nPapel cobre a Pedra')
                    
    
                elif (r == 3) and (c == 1):
                    print('VOCÊ VENCEU\nPedra amassa Tesoura')
                    
                elif (r == 3) and (c == 2):
                    print('VOCÊ VENCEU\nTesoura corta Papel')
                    
                elif (r == 3) and (c == 4):
                    print('VOCÊ VENCEU\nTesoura decapta Lagarto')
                    
                elif (r == 3) and (c == 5):
                    print('O Computador VENCEU\nSpock quebra a Tesoura')
                    
    
                elif (r == 4) and (c == 1):
                    print('VOCÊ PERDEU\nPedra esmaga Lagarto')
                    
                elif (r == 4) and (c == 2):
                    print('VOCÊ VENCEU\nLagarto come Papel')
                    
                elif (r == 4) and (c == 3):
                    print('VOCÊ PERDEU\nTesoura decapta Lagarto')
                    
                elif (r == 4) and (c == 5):
                    print('VOCÊ VENCEU\nLagarto envenena Spock')
                    
    
                elif (r == 5) and (c == 1):
                    print('EMPATE\nSpock valoriza a Pedra, todos saem ganhando')
                    
                elif (r == 5) and (c == 2):
                    print('VOCE PERDEU\nPapel refuta Spock')
                    
                elif (r == 5) and (c == 3):
                    print('VOCÊ VENCEU\nSpock quebra a Tesoura')
                    
                elif (r == 5) and (c == 4):
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