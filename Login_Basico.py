print(' -= ' * 8)
print(' > Bem vindo ao nosso site! <')
print(' -= ' * 8)

print(" \n ")

usuarios_cadastrados = []

#Definindo a função para cadastro de user
def cadastrar_usuario():
    nome_de_usuario = input(" Digite um nome de usuário: ")
    senha = input(" Digite uma senha: ")
    usuarios_cadastrados.append({" nome_de_usuario ": nome_de_usuario, " senha ": senha})
    print(" Usuário cadastrado com sucesso! ")

#Definindo a função para login
def fazer_login():
    nome_de_usuario = input(" Digite o nome de usuário: ")
    senha = input(" Digite a senha: ")
    for usuario in usuarios_cadastrados:
        if usuario[" nome_de_usuario "] == nome_de_usuario and usuario[" senha "] == senha:
            print(" Login bem-sucedido! ")
            return
    print(" Nome de usuário ou senha inválidos. ")

#Definindo a função para exibir o menu
def exibir_menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        opcao = input(" > Resposta: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print(" Até logo! ")
            break
        else:
            print(" Opção inválida. ")


if __name__ == '__main__':
    exibir_menu()
