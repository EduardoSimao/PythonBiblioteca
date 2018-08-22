#-*- encoding utf-8 *-
import os

def cadastrarUsuario():
    nome = input('Digite o nome do Usuario: ')
    idade = int(input('Digite a idade do usuario: '))
    endereco = input('Digite o endereço do usuario: ')
    endereco_num = int(input('Digite o numero da residencia: '))
    tel = input('Digite o telefone: (ddd) xxxx-xxxx ')

    arquivo = open('Leitores/{}.txt'.format(nome),'w')
    arquivo.write('{}\n'.format(nome))
    arquivo.write('{}\n'.format(idade))
    arquivo.write('{}\n'.format(endereco))
    arquivo.write('{}\n'.format(endereco_num))
    arquivo.write('{}\n'.format(tel))
    arquivo.close()

    print('{} cadastrado com sucesso!\n'.format(nome))

def alterarUsuario():
    info = []
    pasta = 'Leitores'
    arquivos = os.listdir(pasta)
    nome = input('Digite o nome do usuario que deseja alterar: ')

    for arquivo in arquivos:
        if arquivo == '{}.txt'.format(nome):          
            idade = int(input('Digite a nova idade do usuario: '))
            endereco = input('Digite o novo endereço do usuario: ')
            endereco_num = int(input('Digite o novo numero da residencia: '))
            tel = input('Digite o novo telefone: (ddd) xxxx-xxxx ')

            arquivo = open('{}/{}.txt'.format(pasta,nome), 'w')
            arquivo.write('{}\n'.format(nome))
            arquivo.write('{}\n'.format(idade))
            arquivo.write('{}\n'.format(endereco))
            arquivo.write('{}\n'.format(endereco_num))
            arquivo.write('{}\n'.format(tel))
            arquivo.close()

            print('{} cadastrado com sucesso!\n'.format(nome))
        else:
            print('Usuario {} nao encontrado\n'.format(nome))

def pesquisarUsuario():
    info = []
    pasta = 'Leitores'  
    arquivos = os.listdir(pasta)

    nome = input('Digite o nome do usuario: ')
    for arquivo in arquivos:
        if arquivo == '{}.txt'.format(nome):
            usuario = open('{}/{}.txt'.format(pasta,nome),'r')
            for dados in usuario:
                info.append(dados)
            print('Nome:{} \nIdade:{} \nEndereço:{} \nNumero da Residencia:{} \nTelefone:{}\n'.format(info[0:1],info[1:2],info[2:3],info[3:4],info[4:]))
        else:
            print('Usuario {} não encontrado!\n'.format(nome))

