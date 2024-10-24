
from clienteService import Cliente
from produtoService import Produto
from autenticacaoService import Autenticacao

# Atribuindo constantes
FINALIZAR_PROGRAMA = "0"
CLIENTES = "clientes"
PRODUTOS = "produtos"

# Instanciando classes
clienteService = Cliente()
produtoService = Produto()
autenticacaoService = Autenticacao()

def main():

  while True:
    print("Seja bem vindo ao Gerenciamento de cadastro de Clientes e Produtos!")
    print("Realize seu Login")

    usuarioLogin = input("Digite seu usuário: ")
    senhaLogin = input("Digite sua senha: ")

    acessoLiberado = autenticacaoService.autenticar(usuarioLogin, senhaLogin)

    if acessoLiberado:
      gerenciamentoDeCadastro()
      break
    else:
      deveContinuar = input("Digite 0 para sair ou pressione qualquer tecla para continuar ")
      if(deveContinuar != FINALIZAR_PROGRAMA):
        continue
      else:
        break

def gerenciamentoDeCadastro():
  print("Neste programa você pode realizar as 4 funções básicas para cliente e produto que são: ")
  print("Adicionar, Editar, Consultar e Remover")

  while True:
    print("=========================") # Separador para ficar com melhor visibilidade no terminal    
    opcao = input("Deseja realizar ação para qual gerenciamento? (1 - Cliente, 2 - Produto ou 0 - para finalizar o programa) ")

    if opcao == "1":
      acao = realizarCrudCliente()
      if acao == FINALIZAR_PROGRAMA:
        break
      else:
        continue   
    elif opcao == "2":
      acao = realizarCrudProduto()
      if acao == FINALIZAR_PROGRAMA:
        break
      else:
        continue  
    elif opcao == FINALIZAR_PROGRAMA:
      break
    else:  
      print("Opção inválida!")
      continue

def mensagemOpcaoCliente(opcao):
  print("=========================") # Separador para ficar com melhor visibilidade no terminal    
  print(f"Você entrou no gerenciamento de {opcao}")
  print("Digite o código para seguir com a ação")
  print("1 - Adicionar")
  print("2 - Editar")
  print("3 - Consultar")
  print("4 - Remover")
  print("9 - Voltar o menu")
  print("0 - Finalizar o programa")

  acao = input("Qual ação deseja realizar? ")
  return acao

def realizarCrudCliente():
  while True:
    acao = mensagemOpcaoCliente(CLIENTES)

    if acao == "1":
      clienteService.adicionarCliente()
    elif acao == "2":
      clienteService.editarCliente()
    elif acao == "3":
      clienteService.consultarCliente()
    elif acao == "4":
      clienteService.removerCliente()
    elif acao == "9":
      break
    elif acao == FINALIZAR_PROGRAMA:
      return FINALIZAR_PROGRAMA
    
    continue

def realizarCrudProduto():
  while True:
    acao = mensagemOpcaoCliente(PRODUTOS)

    if acao == "1":
      produtoService.adicionarProduto()
    elif acao == "2":
      produtoService.editarProduto()
    elif acao == "3":
      produtoService.consultarProduto()
    elif acao == "4":
      produtoService.removerProduto()
    elif acao == "9":
      break
    elif acao == FINALIZAR_PROGRAMA:
      return FINALIZAR_PROGRAMA
    
    continue

if __name__ == "__main__":
  main()
