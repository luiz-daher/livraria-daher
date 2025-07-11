#Mensagem de Boas-Vindas
print("Seja bem-vindo a Livraria Daher!")

#Lista que vai armazenar os dicionários com os dados de cada livro
lista_livro = []

#Variável global para controlar o ID de cada livro
id_global = 0

#Função que cadastrará um novo livro
def cadastrar_livro(id):
    print('-' * 50)
    print("-" * 14 + " MENU CADASTRAR LIVRO " + "-" * 14)
    print(f"ID do livro: {id}")
    #Aqui, o usuário deve colocar as infos sobre o livro
    nome = input("Nome do livro: ")
    autor = input("Autor do livro: ")
    editora = input("Editora do livro: ")

    #Dicionário com os dados do livro
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    #Adiciona o dicionário do livro na lista principal
    lista_livro.append(livro)
    print("Livro cadastrado com sucesso!\n")

#Função que consulta os livros de formas diversas
def consultar_livro():
    #Laço de repetição até o usuário optar por sair
    while True:
        print('-' * 50)
        print("-" * 16 + " MENU DE CONSULTA " + "-" * 16)
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por ID")
        print("3 - Consultar Livro(s) por Autor")
        print("4 - Retornar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        #Consulta todos os livros cadastrados
        if opcao == "1":
            print("\n--- Todos os Livros Cadastrados ---")
            for livro in lista_livro:
                print(f"ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}\n")

        #Consulta por ID
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_busca:
                        print("\n--- Livro Encontrado ---")
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro com este ID não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        #Consulta por nome do autor
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ").strip().lower()
            encontrados = [livro for livro in lista_livro if livro['autor'].strip().lower() == autor_busca]
            if encontrados:
                print(f"\n--- Livros do Autor '{autor_busca}' ---")
                for livro in encontrados:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}\n")
            else:
                print("Nenhum livro encontrado para este autor.")

        #Retorna ao menu inicial
        elif opcao == "4":
            break  # Retorna ao menu principal

        #Validação de entradas erradas
        else:
            print("Opção inválida. Tente novamente.")

#Função de remoção de livros a partir do ID
def remover_livro():
    while True:
        try:
            print('-' * 50)
            print("-" * 15 + " MENU REMOVER LIVRO " + "-" * 15)
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro['id'] == id_remover:
                    lista_livro.remove(livro)
                    print(f"Livro com ID {id_remover} removido com sucesso!\n")
                    return #Encerra a função pós remoção
            print("Id inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

#Menu principal com as opções e um loop
while True:
    print('-' * 50)
    print("-" * 17 + " MENU PRINCIPAL " + "-" * 17)
    print('Escolha a opção desejada:')
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")

    escolha = input(">> ")

    if escolha == "1":
        id_global += 1
        cadastrar_livro(id_global)

    elif escolha == "2":
        consultar_livro()

    elif escolha == "3":
        remover_livro()

    elif escolha == "4":
        print("Encerrando o programa...")
        print("Obrigado por utilizar a Livraria Daher!")
        break #Sai do loop e encerra o programa

    #Valida entradas erradas
    else:
        print("Opção inválida. Tente novamente.")
