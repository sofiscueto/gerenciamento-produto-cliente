import http.client
import json

def verificarCotacaoEmReais():
    #Obtendo os valores
    procoDollar, precoEuro, precoBitCoin = buscarPrecoDasMoedas()

    #Apresentar os resultados
    print(f"Preço do BitCoin: {formatar_valor(float(precoBitCoin))}")
    print(f"Preço do Dólar: {formatar_valor(float(procoDollar))}")
    print(f"Preço do Euro: {formatar_valor(float(precoEuro))}")
    return

#Função para formatar o valor
def formatar_valor(valor):
    return (f"R$ {valor:,.2f}".replace(".", "x").replace(".", ".").replace("x", "."))

def buscarPrecoDasMoedas():
    awesomeapi = http.client.HTTPSConnection("economia.awesomeapi.com.br")
    awesomeapi.request("GET", "/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    response = awesomeapi.getresponse()
    data = response.read()
    cotacoes = json.loads(data)
    return cotacoes["USDBRL"]["bid"], cotacoes["EURBRL"]["bid"], cotacoes["BTCBRL"]["bid"]

verificarCotacaoEmReais()


