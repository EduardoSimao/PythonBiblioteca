#-*- encoding utf-8 *-
import gerenciarLivro
import gerenciarUsuario

op = 1
while op != 0:
    op = int(input('Digite a opção desejada: \n1.Gerenciar Livro \n2.Gerenciar Usuario \n0.sair\n'))

    if op == 1:
        while op != 0:
            op = int(input('Digite a opção desejada: \n1.Cadastar Livro \n2.Alterar Livro \n3.Excluir Livro \n4.Pesquisar Livro \n0.Cancelar\n'))

            if op == 1:
                gerenciarLivro.cadastrar()
            elif op == 2:
                gerenciarLivro.alterar()
            elif op == 3:
                gerenciarLivro.excluir()
            elif op == 4:
                gerenciarLivro.pesquisar()
            elif op == 0:
                print('Operação cancelada\n')
                op = 1
            else:
                print('Opção Invalida!\n')
    elif op == 2:
        while op != 0:
            op = int(input('Digite a opção desejada: \n1.Cadastar Usuario \n2.Alterar Usuario \n3.Pesquisar Usuario \n0.Cancelar\n'))

            if op == 1:
                gerenciarUsuario.cadastrarUsuario()
            elif op == 2:
                gerenciarUsuario.alterarUsuario()
            elif op == 3:
                gerenciarUsuario.pesquisarUsuario()
            elif op == 0:
                print('Operação cancelada\n')
                op = 1
            else:
                print('Opção Invalida!\n')
    elif op == 0:
            print('Operação cancelada\n')
    else:
        print('Opção Invalida!\n')
