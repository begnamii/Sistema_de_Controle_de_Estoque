# Ajudei algumas pessoas. Não passei meu código, mas ajudei a fazer.
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
        print(lista)

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

def estoqueMinimo():
    for i in range(len(estoque)):
        if estoque[i][2] < 5:
            print("Alerta!!!")
            print("Os seguintes produtos estão com menos do que 5 unidades: ")
            print(estoque[i])
            print("Necessidade de reposição! 🚛")

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
        excluir = input("Você deseja excluir esse produto? (s/n): ")
        if excluir == "s":
            estoque.pop(linhaProcurada)
            print("Produto excluído com sucesso! 🗑️")
        elif excluir == "n":
            print("Exclusão cancelada!")
        else:
            print("Esse caractere não corresponde a nenhuma das opções, produto não excluído.")

print("\nSistema de Controle de Estoque Simplificado (SCES)")
print("\nBem vindo ao menu interativo. Por favor selecione uma opção: ")
while True:
    print("\n1- Adicionar produto | 2- Listar todos os produtos | 3- Buscar Produto por ID | 4- Atualizar estoque | 5 - Estoque mínimo | 6- Excluir produto | 7 - Sair")
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
        print("Menu encerrado!")
        break
    else:
        print("Esse caractere não corresponde a nenhuma das opções, tente novamente.")