from random import randint
num = 0
def menu():
    print('[1] gerar soma')
    print('[2] gerar subtração')
    print('[3] gerar multiplicação')
    print('[4] gerar divisão')
    print('[5] para sair')
    num = int(input())
    if num == 5:
        breakpoint()
    if num == 1:
        soma()
    if num == 2:
        sub()
    if num == 3:
        mult()
    if num == 4: 
        divi()


def soma():
    resp = 1
    print('type "exit" to exit')
    while resp != 'exit':
        num1 = randint(0,599)
        num2 = randint(0, 599)
        s = num1+num2
        resp = str(input(f'{num1} + {num2} = '))
        if resp == str(s):
            print('--yes--')            
        else:
            print('--no--')
            print(num1+num2)

def sub():
    resp = 1
    print('type "exit" to exit')
    while resp != 'exit':
        num1 = randint(0,599)
        num2 = randint(0, 599)

        if num1 > num2:
            s = num1-num2
            resp = int(input(f'{num1} - {num2} = '))
            if resp == str(s):
                print('--yes--')
            else:
                print('--fuck--')
        else:
            s = num2-num1
            resp = input(f'{num2} - {num1} = ')
            if resp == str(s):
                print('--yes--')
            else:
                print('--no--')

def mult():
    resp = 1
    print('type "exit" to exit')
    while resp != 'exit':
        num1 = randint(0,10)
        num2 = randint(0, 15)
        s = num1*num2
        resp = input(f'{num1} x {num2} = ')
        if resp == str(s):
            print('--yes--')
        else:
            print('--no--')

def divi():
    resp = 1
    print('type "exit" to exit')
    while resp != 'exit':
        num1 = randint(0,50)
        num2 = randint(0,50)
        if num1 > num2:
            s = num1/num2
            resp = input(f'{num1} / {num2} = ')
            if round(2,resp) == str(s):
                print('--yes--')
            else:
                print('--no--')
                print(s)
        else:
            s = num2/num1
            resp = input(f'{num2} / {num1} = ')
            if round(2,resp) == str(s):
                print('--yes--')
            else:
                print('--no--')
                print(s)

