#criando uma calculadora
import time
res = 0
print('-'*30)
print('\033[1mCalculadora Simples\033[0m'.center(40)) #titulo em negrito
print('-'*30)
time.sleep(1) #intervalo entre a exibição do título e o conteúdo
while True:
    n1 = float(input('Digite um número: '))
    operador = str(input('Digite o operador (+, -, *, /): ')).strip()[0]
    n2 = float(input('Digite um número: '))
    if operador == '+': #somar
       res = n1 + n2
    elif operador == '-': #subtrair
        res = n1 - n2
    elif operador == '*': #multiplicar
        res = n1 * n2
    elif operador == '/': #dividir
        res = n1 / n2
    else:
        print('Dados inválidos, tente novamente!') #caso algo dado tenha sido colocado de forma errônea, irá retornar ao início
    print(f'O resultado é = \033[1;34m{res:.2f}\033[0m')
    time.sleep(1)
    pergunta = input('Quer continuar? \033[1;32mSim\033[0m ou \033[1;31mNão\033[0m: ').upper().strip()[0]
    if pergunta != 'S':
        print('\033[1mVolte sempre\033[0m!')
        break

