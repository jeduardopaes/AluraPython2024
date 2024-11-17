import os, platform


def exibir_nome_programa():
    print(
        """
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █ █ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """
    )


def finalizar_app():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("Finalizando o app ...")
    exit()


def exibir_opcoes():
    while True:
        print("1. Cadastrar Restaurante")
        print("2. Listar Restaurante")
        print("3. Ativar Restaurante")
        print("4. Sair\n")

        opcao_escolhida = int(input("Escolha uma opção: "))
        os.system("cls")

        # print(f"Você escolheu a opção: {opcao_escolhida}")

        if opcao_escolhida == 1:
            print("Cadastrar Restaurantes")
        elif opcao_escolhida == 2:
            print("Listar Restaurantes")
        elif opcao_escolhida == 3:
            print("Ativar Restaurantes")
        elif opcao_escolhida == 4:
            finalizar_app()
            break
        else:
            print("Opção Inválida.")


def main():
    exibir_nome_programa()
    exibir_opcoes()


if __name__ == "__main__":
    main()
