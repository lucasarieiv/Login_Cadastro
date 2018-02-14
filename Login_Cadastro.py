#! python3

import os

def resPass():
    print('Digite 1- Para Se Cadastrar') #Printa Esse texto
    print('Digite 2- Para Fazer Login')
    resp = input() #Essa Linha ta uma entrada
    return resp

resp = resPass() #resp pode ter sido 1 ou 2

while True:
    if resp == '1': #comprando resp com um
        print('Bem Vindo - Área de Cadastro')
        Usuario = input('Usuário: ') #Se nome Lucas
        # LENDO LISTA
        tUsuarios = open('Cadastros\\TodosUsuarios.txt', 'r')
        nUsuario = tUsuarios.read()
        for user in nUsuario.split('\n'):
            while user == Usuario:
                print('Esse Username Já Existe Tente Outro')
                user = input('Usuário: ')
                if user != Usuario:
                    tUsuarios = open('Cadastros\\TodosUsuarios.txt', 'a')
                    nUsuarios = tUsuarios.write(user + '\n')
                    tUsuarios.close()
            tUsuarios = open('Cadastros\\TodosUsuarios.txt', 'a')
            nUsuarios = tUsuarios.write(Usuario + '\n')
            tUsuarios.close()
        tUsuarios.close()

        Email = input('Email: ')
        Password1 = input('Senha: ')
        Password2 = input('Senha Novamente: ')
        if Password1 == Password2:
            Pessoa = open('Cadastros\\'+ Usuario + '.txt', 'a')
            contPessoa = Pessoa.write(Usuario + '\n' + Email + '\n' + Password1)
            Pessoa.close()
            print('Cadastrado Com Sucesso!')
            resp = resPass()
        elif Password1 != Password2:
            while Password1 != Password2:
                print('Suas Senhas Não Estão Iguais')
                print('Digite Sua Senha: ')
                Password1 = input()
                print('Digite Sua Senha Novamente: ')
                Password2 = input()
            Pessoa = open('Cadastros\\'+ Usuario + '.txt', 'a')
            contPessoa = Pessoa.write(Usuario + '\n' + Email + '\n' + Password1)
            Pessoa.close()
            print('Cadastrado Com Sucesso!')
            resp = resPass()
    elif resp == '2':
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
