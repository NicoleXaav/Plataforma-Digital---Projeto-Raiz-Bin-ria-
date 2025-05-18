import json
import os
import hashlib
from conteudo_educativo import CONTEUDOS

ARQUIVO = "dados_usuarios.json"

def ler_usuarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    return []

def gravar_usuarios(lista):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(lista, arquivo, indent=2)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_usuario(email, usuarios):
    for usuario in usuarios:
        if usuario["email"] == email:
            return True
    return False

def registrar_usuario():
    print("\n--- Novo Cadastro ---\n")
    print("Aviso: Seus dados serão tratados conforme a LGPD (Lei Geral de Proteção de Dados).")
    print("Eles serão usados apenas para fins de autenticação na plataforma.\n")
    print("========================================\n")
    nome = input("Informe seu nome: ")
    idade = input("Informe sua idade: ")
    email = input("Digite seu e-mail: ")
    senha = input("Crie uma senha segura: ")
    print()

    usuarios = ler_usuarios()

    if verificar_usuario(email, usuarios):
        print("Este e-mail já está cadastrado.")
        print("\n========================================")
        return "duplicado"

    novo = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": hash_senha(senha)
    }

    usuarios.append(novo)
    gravar_usuarios(usuarios)
    print("\nCadastro feito com sucesso!")
    print("\n========================================")
    return True

def login_usuario():
    print("\n--- Acesso à Plataforma Digital ---\n")
    email = input("E-mail: ")
    senha = input("Senha: ")
    print()

    usuarios = ler_usuarios()
    senha_criptografada = hash_senha(senha)

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha_criptografada:
            print(f"Login realizado. Bem-vindo(a), {usuario['nome']}!")
            print("\n========================================")
            return True

    print("Dados incorretos.")
    print("\n========================================")
    return False

def mostrar_conteudo():
    while True:
        print("\n--- Portal Educativo ---\n")
        print("1 - Lógica de Programação")
        print("2 - Python Básico")
        print("3 - Cibersegurança")
        print("4 - Práticas e Avaliações")
        print("5 - Encerrar\n")
        
        escolha = input("Escolha uma opção: ")
        print("\n========================================\n")

        if escolha == "5":
            print("Encerrando sessão")
            print("\n========================================")
            break
        elif escolha in CONTEUDOS:
            print(CONTEUDOS[escolha])
            input("Pressione Enter para continuar...")
        else:
            print("Opção inválida. Tente novamente.")
        print("\n========================================")


def menu_principal():
    while True:
        print("\n--- Bem-vindo ao Portal Educativo ---")
        print("1 - Login")
        print("2 - Cadastro")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            if login_usuario():
                mostrar_conteudo()
        elif escolha == "2":
            registrar_usuario()
        elif escolha == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
