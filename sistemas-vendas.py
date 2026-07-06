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

carrinho = []


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
        for chave, valor in estoque_produtos.items():
            print(f"{chave}:{valor}")

    elif opcao == 2:
        print("adicionando itens os carrinho")
        id_produto = int(input("qual id do produto você deseja comprar?"))
        if id_produto in estoque_produtos:
            qtd_produto =int(input("quantas unidades voce deseja?"))
            if qtd_produto <= 0:
                print("Quantidade invalida")
            elif qtd_produto <= estoque_produtos [id_produto]["quantidade"]:
                carrinho.append(estoque_produtos[id_produto])
                estoque_produtos[id_produto]["quantidade"]-= qtd_produto
    elif opcao == 3:
        if carrinho:
        print("visualizando carrinho")
        subtotal = 0
        for i in carrinho:
            print(f"{i["qtd"]}x{i["nome"]} no valor de R$ {i["preco"]}(cada)\nTotal R${i["preco_total"]}")
           subtotal += i["preco_total"]
        print(f"Subtotal da compra R${subtotal}")
    elif opcao == 4:
        print("finalizando compra")
        if not carrinho:
            print("seu carrinho está vazio")
        else:
            desconto = 0
            cupom = input("digite um cupom valido")
            if cupom == "DEV10":
                desconto = subtotal * 0.1
                print("cupom de 10%")
            elif cupom == "DEV20" and subtotal > 500:
                desconto = subtotal * 0.2
                print("cupom de 20%")
            elif len(cupom) == 0:
                print("nenhum cupom foi adicionado")
            else:
                print("Cupom invalido")
                print("-------RESUMO DO PEDIDO-------")
                print(f" Subtotal da Compra :  R${subtotal:.2f}")
                print(f" Desconto :  R${desconto:.2f}")
                print(f" Valor final : R${subtotal - desconto :.2f}")
                print("-" * 30)
                finalizar = input("deseja finalizar a compra s/n:")
                if finalizar == 's':
                    carrinho.clear()
                else:
                    print("compra finalizada. Saindo do sistema...")
                    break

    elif opcao == 0:
        print("sistema encerrado...")
        break
    else:
        print("opção invalida")
