from Cadastro import *
import os

def resPass():
    print('Digite 1- Para Fazer Login') #Printa Esse texto
    print('Digite 2- Para Cadastrar')
    print('Digite 3- Para Sair')
    resp = input() #Essa Linha ta uma entrada
    return resp

while True:
    resp = resPass()
    if resp == '1':
        print('Bem Vindo Ao Nosso Programa')
        login = input('Digite Seu Login: ')
        for u in os.listdir('Cadastros\\'):
            if (login.upper() + '.txt') == u:
                senha = input('Digite Sua Senha: ')
                uLog = open('Cadastros\\' + u, 'r')
                cLog = uLog.read()
                cont = 0
                for ul in cLog.split('\n'):
                    cont += 1
                    if cont == 3:
                        if ul == senha.upper():
                            print('Bem Vindo')
                        elif ul != senha.upper():
                            while ul != senha.upper():
                                print('Senha Incorreta!')
                                senha = input('Digite Sua Senha Novamente: ')
                            print('Bem Vindo!')
                uLog.close()
    elif resp == '2':
        cadastroPessoas()

    elif resp == '3':
        break
