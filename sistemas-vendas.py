estoque_produtos = {
    1: {"nome":"Tênis Nike Revolution 8 Masculino", "preco":299.98,"quantidade":10 },
    2: { "nome":"Tênis Nike Flex Train Masculino", "preco":313.49, "quantidade":10},
    3: { "nome":"Tênis Nike Air Max Alpha Trainer 6 Masculino", "preco":529.91,"quantidade":4},
    4: { "nome":"Tênis Nike Air Max Alpha Trainer 6 Masculino", "preco":539.99,"quantidade":5 },
    5: { "nome":"Tênis Nike Court Vision Low Next Nature Feminino","preco":429.39,"quantidade":7},
    6: { "nome":"Tênis Nike Air Max Bia Masculino", "preco":427.49,"quantidade":3},
    7: { " nome":"Tênis Nike Air Max Vigor Masculino","preco":470.24,"quantidade":5},
    8: { "nome":"Tênis Nike Air Max Nuaxis Masculino","preco":398.99,"quantidade":3},
    9: { "nome":"Tênis Nike MC Trainer 3 Feminino","preco":427.49,"quatidade":3 },
    10: { "nome":"Tênis Infantil Nike Revolution 7","preco":299.99,"quantidade":7},
}




while True:
    print("*"*30)
    print("bem vindo ao sistemas de compras")
    print ("(1) visualizar estoque.")
    print ("(2) adicionar itens os carrinho")
    print ("(3) visualizar Carrinho")
    print ("(4) finalizar compra.")
    print ("(5) sair do sistema.")
    opcao = int(input("qual a opcao: "))

    if opcao == 1:
        print("visualizando estoque")
        for k, v in estoque_produtos():

    elif opcao == 2:
        print("adicionando itens os carrinho")
    elif opcao == 3:
        print("visualizando carrinho")
    elif opcao == 4:
        print("finalizando compra")
    elif opcao == 5:
        print("sistema encerrado")
        break
    else:
        print("opção invalida")
