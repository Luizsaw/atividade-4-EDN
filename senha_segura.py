def senha_segura(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

senha = input("Digite uma senha: ")

if senha_segura(senha):
    print("Senha válida e segura.")
else:
    print("Senha inválida. Ela deve ter pelo menos 8 caracteres e conter ao menos um número.")