# Ajudei algumas pessoas a fazer, algumas delas são: Murilo, Miguel, Gustavo Dias, Gustavo Terassi, Vithor Armando, João Pitanguy. OBS: Não passei meu código.
estoque = [
    [1, "Celular", 3, "Prateleira A"],
    [2, "Carregador", 14, "Prateleira A"],
    [3, "Fone", 7, "Prateleira B"],
]
proximoId = 4
    
def travarMenu():
    input("\nPressione <ENTER> para continuar...")

def adicionarProduto():
    global proximoId, novoProduto, quantidadeEstoque, localizacaoProduto
    novoProduto = input("Qual o novo produto?: ")
    quantidadeEstoque = int(input("Qual a quantidade desse produto no estoque?: "))
    localizacaoProduto = input("Qual a localização do produto?: ")
    estoque.append([proximoId, novoProduto, quantidadeEstoque, localizacaoProduto])
    proximoId += 1
    print("\nProduto adicionado com sucesso! 📦\n")
    travarMenu()

def listarProdutos():
    print("Os produtos diponíveis no estoque são: ")
    for lista in estoque:
        print(lista)
    travarMenu()

def buscarProduto():
    buscarId = int(input("Qual o ID do produto?: "))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if estoque[i][0] == buscarId:
            linhaProcurada = i
    if (linhaProcurada == -1):
        print("Produto não encontrado!")
    else:
        print(f"Produto encontrado!\nDados do produto: {estoque[linhaProcurada]}")
    travarMenu()

def atualizarEstoque():
    buscarId = int(input("Qual o ID do produto que será atualizado?: "))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if estoque[i][0] == buscarId:
            linhaProcurada = i
    if (linhaProcurada == -1):
        print("Produto não encontrado!")
    else:
        print(f"{estoque[linhaProcurada]}")
        novaQuantidade = int(input(f"Qual a nova quantidade do produto?: "))
        estoque[linhaProcurada][2] = novaQuantidade
        print("Nova quantidade atualizada com sucesso! ♻️")
    travarMenu()

def estoqueMinimo():
    print("Alerta!!! ⚠️")
    print("Os seguintes produtos estão com menos do que 5 unidades: ")
    for i in range(len(estoque)):
        if estoque[i][2] < 5:
            
            print(estoque[i])
    print("Necessidade de reposição! 🚛")
    travarMenu()

def excluirProduto():
    buscarId = int(input("Qual o ID do produto que será excluído?: "))
    linhaProcurada = -1
    for i in range(len(estoque)):
        if estoque[i][0] == buscarId:
            linhaProcurada = i
    if (linhaProcurada == -1):
        print("Produto não encontrado!")
    else:
        print(f"{estoque[linhaProcurada]}")
        excluir = input("Você deseja excluir esse produto? (s/n): ").lower()
        if excluir == "s":
            estoque.pop(linhaProcurada)
            print("Produto excluído com sucesso! 🗑️")
        elif excluir == "n":
            print("Exclusão cancelada!")
        else:
            print("Esse caractere não corresponde a nenhuma das opções, produto não excluído.")
    travarMenu()

print("\nSistema de Controle de Estoque Simplificado (SCES)")
print("\nBem vindo ao menu interativo. Por favor selecione uma opção: ")
while True:
    print("\n1- Adicionar produto | 2- Listar todos os produtos | 3- Buscar produto por ID | 4- Atualizar estoque | 5 - Estoque mínimo | 6- Excluir produto | 7 - Sair")
    opçao = input("Escolha: ")
    print("\n")
    if (opçao == "1"):
        adicionarProduto()
    elif (opçao == "2"):
        listarProdutos()
    elif(opçao == "3"):
        buscarProduto()
    elif(opçao == "4"):
        atualizarEstoque()
    elif(opçao == "5"):
        estoqueMinimo()
    elif(opçao == "6"):
        excluirProduto()
    elif(opçao == "7"):
        print("Menu encerrado! ❌")
        break
    else:
        print("Esse caractere não corresponde a nenhuma das opções, tente novamente.")