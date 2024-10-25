import http.client
import json
import pandas as pd

class EnderecoApiService:

    def consultarEnderecoIbge(self, cep=None):
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")

        while True:
            #Solicitar o Cep ao usuário
            cep = input("Digite o cep para consultar o endereço: ")

            #Enviar uma requisição
            apiViaCep.request("GET", f"/ws/{cep}/json/")

            #Obter uma resposta
            response = apiViaCep.getresponse()

            data = response.read().decode("utf-8")
            endereco = json.loads(data)

            endereco_simples = [
                {
                "logradouro": endereco.get("logadouro"),
                "bairro": endereco.get("bairro"),
                "localidade": endereco.get("localidade"),
                "uf": endereco.get("uf")
                }
            ]

            endereco_json = json.dumps(endereco_simples, indent=4)

            tabela = pd.DataFrame(endereco_json)
            print(tabela)
            break

servico = EnderecoApiService()
servico.consultarEnderecoIbge()