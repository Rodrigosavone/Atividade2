def main():
    listaDados = []
    opcao = menu()
    while(opcao <= 6):
        if (opcao == 1):
            cadastro(listaDados)
            opcao = menu()
        elif (opcao == 2):
            listarUsuariosPorOrdemCadastro(listaDados)
            opcao = menu()
        elif (opcao == 3):
            listarUsuarioPorOrdemAlfabetica(listaDados)
            opcao = menu()
        else:
            print('Opção invalida escolha novamente:')
            opcao = menu()

def menu():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Sistema de Inscrições')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('1 - Cadastrar novo usuário')
    print('2 - Listar usuários cadastrados por ordem de cadastro')
    print('3 - Listar usuários cadastrados por ordem alfabética')
    print('4 - Buscar usuário')
    print('5 - Remover usuário')
    print('6 - Alterar nome do usuário')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    opcao = int(input('Escolha uma opção: '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    return opcao

def cadastro(listaDados):
    dados = dict()
    dados['nome'] = input('Nome completo: ').upper()
    dados['email'] = input('E-mail: ').upper()
    listaDados.append(dados)

def listarUsuariosPorOrdemCadastro(listaDados):
    for dados in listaDados:
        print('Nome:', dados['nome'] , 'E-mail:', dados['email'])

def listarUsuarioPorOrdemAlfabetica(listaDados):
    for usuarios in sorted(listaDados, key = lambda k: k['nome']):
        print('Nome:', usuarios['nome'] , 'E-mail:', usuarios['email'])


if __name__ == '__main__':
    main()