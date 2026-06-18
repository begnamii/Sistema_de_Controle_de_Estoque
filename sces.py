estoque = [
    [1, "Celular", 3, "Prateleira A"],
    [2, "Carregador", 14, "Prateleira A"],
    [3, "Fone", 7, "Prateleira B"],
]
proximoId = 4
    
def adicionarProduto():
    global proximoId, novoProduto, quantidadeEstoque, localizacaoProduto
    novoProduto = input("Qual o novo produto?: ")
    quantidadeEstoque = int(input("Qual a quantidade desse produto no estoque?: "))
    localizacaoProduto = input("Qual a localização do produto?: ")
    estoque.append([proximoId, novoProduto, quantidadeEstoque, localizacaoProduto])
    proximoId += 1
    print("\nProduto adicionado com sucesso! 📦\n")

def listarProdutos():
    print("Os produtos diponíveis no estoque são: ")
    for lista in estoque:
        print(f"{lista}")

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
        print(f"{estoque[linhaProcurada]}")

print("\nSistema de Controle de Estoque Simplificado (SCES)")
print("\nBem vindo ao menu de opções. Por favor selecione uma opção: ")
while True:
    print("\n1- Adicionar produto | 2- Listar todos os produtos | 3- Buscar Produto por ID | 4- Atualizar estoque | 5- Sair")
    opçao = input("Escolha: ")
    if (opçao == "1"):
        adicionarProduto()
    elif (opçao == "2"):
        listarProdutos()
    elif(opçao == "3"):
        buscarProduto()
    elif(opçao == "4"):
        atualizarEstoque()
    elif(opçao == "5"):
        print("Menu encerrado!")
        break
    # else:
    #     print("Esse caractere não corresponde a nenhuma das opções, tente novamente.")