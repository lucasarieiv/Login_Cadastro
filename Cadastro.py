#! python3

def cadastroPessoas():
        print('Bem Vindo - Área de Cadastro')
        Usuario = input('Usuário: ')
        Email = input('Email: ')

        # VALIDANDO O EMAIL
        toEmail = open('Cadastros\\todosEmails.txt', 'r')
        coEmail = toEmail.read()
        for email in coEmail.split('\n'):
            while (Email.upper()) == email:
                print('Usuário já Cadastrado com Esse Email')
                Email = input('Digite um email Válido: ')
        print('Email Valido')
        toEmail.close()

        # ADCIONANDO EMAIL NOVO EM TODOSEMAILS
        tEmail = open('Cadastros\\todosEmails.txt', 'a')
        cEmail = tEmail.write(Email.upper() + '\n')
        tEmail.close()

        # PASSWORD
        Password1 = input('Senha: ')
        Password2 = input('Senha Novamente: ')
        if Password1 == Password2:
            Pessoa = open('Cadastros\\'+ Usuario.upper() + '.txt', 'a')
            contPessoa = Pessoa.write(Usuario.upper() + '\n' + Email.upper() + '\n' + Password1.upper())
            Pessoa.close()
            print('Cadastrado Com Sucesso!')
        elif Password1 != Password2:
            while Password1 != Password2:
                print('Suas Senhas Não Estão Iguais')
                print('Digite Sua Senha: ')
                Password1 = input()
                print('Digite Sua Senha Novamente: ')
                Password2 = input()
            Pessoa = open('Cadastros\\'+ Usuario.upper() + '.txt', 'a')
            contPessoa = Pessoa.write(Usuario.upper() + '\n' + Email.upper() + '\n' + Password1.upper())
            Pessoa.close()
            print('Cadastrado Com Sucesso!')
