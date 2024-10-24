import requests

# URL da API do json-server
url = "http://localhost:3000/clientes"

class ClientesApiService:

    #fazendo a requisição GET
    def buscarClientes(self):
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print("Erro ao acessar a API:", response.status_code)

    #GET com parametro
    def buscarCliente(self, id=None, nome=None, cpf=None):
        if id is not None and nome is not None:
            response = requests.get(f"{url}?id={id}&nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}")
        elif nome is not None:
            response = requests.get(f"{url}?nome={nome}")
        elif cpf is not None:
            response = requests.get(f"{url}?cpf={cpf}")
        else: 
            self.buscarClientes()
            return
        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print("Erro ao acessar a API:", response.status_code)

    #Post sendo enviado o body JSON
    def adicionarCliente(self, nome, cpf):
        novo_cliente = {"nome": nome, "cpf": cpf}
        response = requests.post(url, json=novo_cliente)

        if response.status_code == 201:
            print(F"{nome} foi adicionado a lista de clientes")
        else:
            print("Erro ao adiconar o cliente:", response.status_code)

    #Put sendo enviado o body JSON
    def alterarCliente(self, id, nome, cpf=None):
        cliente_atualizado = {"nome": nome}
        
        if cpf is not None:
            cliente_atualizado["cpf"] = cpf

        response = requests.put(f"{url}/{id}", json=cliente_atualizado)

        if response.status_code == 200:
            print(F"{nome} foi atualizado na lista de clientes")
        else:
            print("Erro ao atualizar o cliente:", response.status_code)

    #Delete via parametro ID
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")

        if response.status_code == 200:
            print(F"Cliente de código {id} foi removido da lista de clientes")
        else:
            print("Erro ao remover o cliente:", response.status_code)

servico = ClientesApiService()
servico.buscarCliente("1")
servico.buscarCliente(None, "Brenda")
servico.buscarCliente(3, "Catarina")
servico.buscarCliente(None, None, "000000004")
# servico.adicionarCliente("Sofia", "000000005")
servico.alterarCliente("307b", "Sofia Cueto", "000000005")
servico.removerCliente("31a1")
