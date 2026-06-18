estoque = [
    [],
]
proximoId = 1
    
def adicionarProduto():
    global proximoId, novoProduto, quantidadeEstoque, localizacaoProduto
    novoProduto = input("Qual o novo produto?: ")
    quantidadeEstoque = int(input("Qual a quantidade desse produto no estoque?: "))
    localizacaoProduto = 1
    estoque.append([proximoId, novoProduto, quantidadeEstoque, localizacaoProduto])
    proximoId = proximoId + 1
    print("\nProduto adicionado com sucesso! 📦\n")

def listarProdutos():
    for lista in estoque:
        print(f"Os produtos diponíveis são: {lista}")

print("\nSistema de Controle de Estoque Simplificado (SCES)")
print("\nBem vindo ao menu de opções. Por favor selecione uma opção: ")
while True:
    print("\n1- Adicionar produto | 2- Listar todos os produtos | 3- Buscar Produto por ID | 4- Atualizar estoque | 5- Sair")
    opçao = input("Escolha: ")
    if (opçao == "1"):
        adicionarProduto()
    elif (opçao == "2"):
        listarProdutos()
    # elif(opçao == "3"):
    #     buscarProduto()
    # elif(opçao == "4"):
    #     atualizarEstoque()
    elif(opçao == "5"):
        print("Menu encerrado!")
        break
    # else:
    #     print("Esse caractere não corresponde a nenhuma das opções, tente novamente.")