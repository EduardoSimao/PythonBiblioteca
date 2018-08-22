import os

def cadastrar():
    nome_livro = input('Digite o nome do livro: ')
    ano = int(input('Digite o ano de lançamento: '))
    nome_autor = input('Digite o nome do Autor: ')
    genero = input('Digite o genero do livro: ')

    arquivo = open('biblioteca/{}.txt'.format(nome_livro), 'w')
    arquivo.write('{}\n'.format(nome_livro))
    arquivo.write('{}\n'.format(ano))
    arquivo.write('{}\n'.format(nome_autor))
    arquivo.write('{}\n'.format(genero))
    
    arquivo.close()
    print('livro cadastrado com sucesso\n')
    
def alterar():
    info = []
    arquivos = 'biblioteca'
    pasta = os.listdir(arquivos)
    nome = input('Digite o nome do livro que deseja alterar: ')
    for arquivo in pasta:
        if arquivo == '{}.txt'.format(nome):
            livro = open('{}/{}.txt'.format(arquivos,nome), 'r')
            for dados in livro:
                info.append(dados)
            print('Ano do livro atual {}'.format(info[1:2]))
            ano = int(input('Digite o novo ano de lançamento: '))

            print('Nome do Autor atual {}'.format(info[2:3]))
            nome_autor = input('Digite o novo nome do Autor: ')

            print('Genero do livro atual {}'.format(info[3:]))
            genero = input('Digite o novo genero do livro: ')

            arquivo = open('biblioteca/{}.txt'.format(nome), 'w')
            arquivo.write('{}\n'.format(nome))
            arquivo.write('{}\n'.format(ano))
            arquivo.write('{}\n'.format(nome_autor))
            arquivo.write('{}\n'.format(genero))

            arquivo.close()
            print('livro alterado com sucesso!\n') 
        else:
            print('Livro {} nao encontrado\n'.format(nome))
     
      

def pesquisar():
    info = []
    pasta = 'biblioteca'
    arquivos = os.listdir(pasta)
    nome = input('Digite o nome do livro que deseja visualizar: ')
    for arquivo in arquivos:
        if arquivo == '{}.txt'.format(nome):
            livro = open('{}/{}.txt'.format(pasta,nome), 'r')
            for dados in livro:
                info.append(dados) 
            print('Livro: {} \nAno: {} \nAutor: {} \nGenero: {}\n'.format(info[0:1],info[1:2],info[2:3],info[3:]))             
        else:
            print('Livro {} nao encontrado'.format(nome))
    

def excluir():
    arquivos = 'biblioteca'
    pasta = os.listdir(arquivos)
    nome = input('Digite o nome do livro que deseja excluir: ')
    for arquivo in pasta:
        if arquivo == '{}.txt'.format(nome):
            os.remove('{}/{}.txt'.format(arquivos,nome))
            print('{} removido com sucesso\n!'.format(nome))
        else:
            print('{} não encontrado!\n'.format(nome))