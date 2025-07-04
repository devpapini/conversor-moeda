#v2

import requests

api_key = "8a7ed66e6b71cf32c3f2d792"

mapa_moedas = {
"euro":"EUR",
"real":"BRL",
"dolar":"USD",
}

def conversao(origem,destino,valor, api_key):

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{origem}"  

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro ao acessar API.")
        return None  

    dados = response.json()

    if dados.get("result") != "success":
        print ("API retornou erro", dados.get("error-type"))
        return None
    
    taxas = dados.get("conversion_rates", {})

    if destino not in taxas:
        print(f"Moeda destino '{destino}' não encontrada nas taxas.")
        return None
    
    taxas = taxas[destino]
    valor_convertido = valor * taxas 
    return valor_convertido 



def inicio():
    while True:
        origemrl = input("Moeda de origem (euro, dolar ou real): ").strip().lower()
        destinorl = input("Moeda de destino (euro, dolar ou real): ").strip().lower()
        valor = input("Valor a ser convertido: ")

        origem = mapa_moedas.get(origemrl)
        if origem is None:
            print(f"Moeda {origemrl} desconhecida! Por favor, tente novamente.")
            continue
        destino = mapa_moedas.get(destinorl)
        if destino is None:
            print(f"Moeda {destinorl} desconhecida! Por favor, tente novamente.")
            continue

        try:
            valor = float(valor)
        except ValueError:
            print("Valor inválido. Digite um número.\n")
            continue

        resultado = conversao(origem, destino, valor, api_key)

        if resultado is not None:
            print(f"Convertendo {valor:.2f} {origemrl} → {destinorl}")
            print(f"Resultado: {resultado:.2f}")
            break
        else:
            print("Conversão inválida! Verifique as moedas digitadas.\n")

inicio()



"""
1. Receber dados do usuário (feito)
Perguntar qual moeda ele quer converter (moeda de origem), por exemplo: USD, BRL, EUR

Perguntar para qual moeda quer converter (moeda de destino)

Perguntar qual valor deseja converter (ex: 100)

Garantir que o valor digitado é um número positivo (pode ser decimal)

2. Fazer a requisição para a API de câmbio (feito)
Usar uma API pública gratuita para pegar a taxa de câmbio atual entre as moedas

Enviar os dados (moeda origem, destino e valor) para a API e receber a resposta com o valor convertido

3. Tratar a resposta da API (feito)
Verificar se a API respondeu corretamente (sem erros)

Pegar o valor convertido do JSON retornado pela API

4. Exibir o resultado para o usuário (feito)
Mostrar na tela o valor convertido formatado com duas casas decimais
Exemplo: 100.00 USD = 540.25 BRL

5. Tratar erros (feito)
Caso a API não responda ou retorne erro, mostrar uma mensagem amigável para o usuário

Caso o usuário digite dados inválidos, avisar e pedir para tentar de novo

"""