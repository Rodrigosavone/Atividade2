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
        elif (opcao == 4):
            buscarUsuario(listaDados)
            opcao = menu()
        elif (opcao == 5):
            removerUsuario(listaDados)
            opcao = menu()
        elif (opcao == 6):
            alterarNome(listaDados)
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
    dados['email'] = input('E-mail: ')
    listaDados.append(dados)

def listarUsuariosPorOrdemCadastro(listaDados):
    for dados in listaDados:
        print('Nome:', dados['nome'] , 'E-mail:', dados['email'])

def listarUsuarioPorOrdemAlfabetica(listaDados):
    for usuarios in sorted(listaDados, key = lambda k: k['nome']):
        print('Nome:', usuarios['nome'] , 'E-mail:', usuarios['email'])

def buscarUsuario(listaDados):
    nome = input('Nome: ')
    find = False
    for buscaNome in listaDados:
        if(buscaNome['nome'] == nome.upper()):
            print('Usuário encontrado')
            print('Nome:', buscaNome['nome'], 'E-mail:', buscaNome['email'])
            find = True
            break
    if find == False:    
        print('Usuário não encontrado')     

def removerUsuario(listaDados):
    email = input('E-mail: ')
    remove = False
    for usuarioDeletado in listaDados:
        if (usuarioDeletado['email'] == email):
            print('Usuário removido: ', usuarioDeletado['nome'])
            listaDados.remove(usuarioDeletado)
            remove = True
    if remove == False:    
        print('Usuário não encontrado')   
        
def alterarNome(listaDados):
    email = input('E-mail: ')
    alter = False
    for dados in listaDados:
        if(dados['email'] == email):
            print('Nome:', dados['nome'] , 'E-mail:', dados['email'])
            nome = input('Digite o nome que deseja alterar: ')
            dados['nome'] = nome
            alter = True
    if alter == False:    
        print('Usuário não encontrado') 

if __name__ == '__main__':
    main()