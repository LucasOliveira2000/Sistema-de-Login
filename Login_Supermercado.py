import psycopg2

# Função para criar a conexão com o banco de dados Supermercado
def create_server_connection():
    try:
        connection = psycopg2.connect(
            dbname = 'Supermercado',
            host='localhost',
            user='postgres',
            password='260600',
            port = '5432'
        )
        print("PostgreSQL connected successfully")
        return connection
    except Exception as err:
        print(f"Error: '{err}'")

# Função para cadastrar usuário no banco de dados
def cadastrar_usuario(connection):
    nome_de_usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    email = input("Digite um email: ")
    data_de_nascimento = input("Digite a data de nascimento (no formato yyyy-mm-dd): ")
    try:
        with connection.cursor() as cursor:
            sql_query = "INSERT INTO usuarios (nome_de_usuario, senha, email, data_de_nascimento) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_query, (nome_de_usuario, senha, email, data_de_nascimento))
            connection.commit()
            print("Usuário cadastrado com sucesso!")
    except Exception as err:
        print(f"Error: '{err}'")

# Função para fazer login no banco de dados
def fazer_login(connection):
    nome_de_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    try:
        with connection.cursor() as cursor:
            sql_query = "SELECT * FROM usuarios WHERE nome_de_usuario=%s AND senha=%s"
            cursor.execute(sql_query, (nome_de_usuario, senha))
            result = cursor.fetchone()
            if result is not None:
                print("Login bem-sucedido!")
            else:
                print("Nome de usuário ou senha inválidos.")
    except Exception as err:
        print(f"Error: '{err}'")

# Função para exibir o menu
def exibir_menu(connection):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        opcao = input(" > Resposta: ")
        if opcao == "1":
            cadastrar_usuario(connection)
        elif opcao == "2":
            fazer_login(connection)
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    connection = create_server_connection()
    exibir_menu(connection)
