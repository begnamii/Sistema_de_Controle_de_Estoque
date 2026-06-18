estoque = [
    [1, "Celular", 3, "Prateleira A"],
    [2, "Carregador", 14, "Prateleira A"],
    [3, "Fone", 7, "Prateleira B"],
]
proximoId = 1
    
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
    global buscarId, localizacaoProduto
    buscarId = int(input("Qual o ID do produto?: "))
    for linha in range(len(estoque)):
        if estoque[linha][0] == buscarId:
            print(f"O produto está na seguinte localização: {localizacaoProduto[linha]}")
        elif estoque[linha][0] != buscarId:
            print("Nenhum produto encontrado com esse ID")

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
    # elif(opçao == "4"):
    #     atualizarEstoque()
    elif(opçao == "5"):
        print("Menu encerrado!")
        break
    # else:
    #     print("Esse caractere não corresponde a nenhuma das opções, tente novamente.")