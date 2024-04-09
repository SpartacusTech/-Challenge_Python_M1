
"""Nesse desafio desenvolveremos uma agenda para salvar, 
editar, deletar e marcar um contato como favorito. O resultado da 
aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”."""


"""Regras da aplicação

- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir 
que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato"""





def salvar_contato(contatos, nomeContato, telefone, email, favorito):
    try:
        contato = {"Nome": nomeContato, "Telefone": telefone,
                   "Email": email, "Favorito": False}
        favorito_maiusculo = favorito.upper()
        if favorito_maiusculo == "SIM":
            contato["Favorito"] = True

        contatos.append(contato)
        print(f"Contato de nome {nomeContato} foi adicionado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o contato: {str(e)}")
    return


def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email, novo_favorito):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if 0 <= indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["Nome"] = novo_nome
            contatos[indice_contato_ajustado]["Telefone"] = novo_telefone
            contatos[indice_contato_ajustado]["Email"] = novo_email
            contatos[indice_contato_ajustado]["Favorito"] = novo_favorito
            print(f"Contato {indice_contato} atualizado")
        else:
            print("Índice de contato inválido")
    except ValueError:
        print("Índice de contato inválido (deve ser um número inteiro)")
    return


def ver_contatos(contatos):
    try:
        print("\nLista de Contatos:")
        for indice, contato in enumerate(contatos, start=1):
            favorito = "*" if contato["Favorito"] else ""
            nome_contato = contato["Nome"]
            telefone_contato = contato["Telefone"]
            email_contato = contato["Email"]
            print(f"{indice}. Nome: [{nome_contato}] Telefone: [{telefone_contato}] Email: [{email_contato}] {favorito}")
    except Exception as e:
        print(f"Ocorreu um erro ao exibir os contatos: {str(e)}")


def deletar_contato(contatos, indice_contato):
    try:
        indice_contato = int(indice_contato) - 1
        if 0 <= indice_contato < len(contatos):
            contato_deletado = contatos.pop(indice_contato)
            print(f"Contato {contato_deletado['Nome']} deletado com sucesso!")
        else:
            print("Índice de contato inválido")
    except ValueError:
        print("Índice de contato inválido (deve ser um número)")     


contatos = []
while True:
    print("\nMenu de gerenciar de Agenda")
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Visualizar Contato")
    print("4. Deletar Contato")
    print("5. Sair")

    escolha = input("Digite o que deseja fazer: ")

    if escolha == "1":
        nomeContato = input("Digite o nome do Contato: ")
        telefone = input("Digite o Telefone do Contato: ")
        email = input("Digite o E-mail do Contato: ")
        favorito = input("Deseja Favoritar o Contato? (Sim/Nao)")
        salvar_contato(contatos, nomeContato, telefone, email, favorito)

    elif escolha == "2":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o nome do contato que deseja atualizar (ou aperte a tecla Enter para pular): ")
        if novo_nome == "":
            novo_nome = contatos[int(indice_contato) - 1]["Nome"]

        novo_telefone = input("Digite o telefone do contato que deseja atualizar (ou aperte a tecla Enter para pular): ")
        if novo_telefone == "":
            novo_telefone = contatos[int(indice_contato) - 1]["Telefone"]

        novo_email = input("Digite o email do contato que deseja atualizar (ou aperte a tecla Enter para pular): ")
        if novo_email == "":
            novo_email = contatos[int(indice_contato) - 1]["Email"]

        novo_favorito = input("Digite Sim/Nao para favoritar contato (ou aperte a tecla Enter para pular): ")
        if novo_favorito == "":
            novo_favorito = contatos[int(indice_contato) - 1]["Favorito"]

        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email, novo_favorito)


    elif escolha == "3":
        ver_contatos(contatos)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
        ver_contatos(contatos)

    elif escolha == "5":
        break
