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
        print('Digite Seu Login:')
        login = input()
        print('Digite Sua Senha')
        userPass = input()
        for key, value in user.items():
            if login == key and userPass == value:
                print('Logado Com Sucesso')
                break
            else:
                print('Você Não Se Encontra Cadastrado no Banco de Dados')
                resp = resPass()
    elif resp == '2':
        cadastroPessoas()

    elif resp == '3':
        break
