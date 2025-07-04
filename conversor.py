#v1

def conversao(origem,destino,valor):
    taxas ={
        ("euro","dolar"):1.18,
        ("euro","real"):6.37,
        ("dolar","euro"):0.85,
        ("dolar","real"):5.41,
        ("real","euro"):0.16,
        ("real","dolar"):0.18,

    }

    chave = (origem, destino)

    if chave in taxas:
        return valor * taxas[chave]
    elif origem == destino:
        return valor
    else:
        return None
    
def inicio():
    while True:
        origem = input("Moeda de origem (euro, dolar ou real): ").strip().lower()
        destino = input("Moeda de destino (euro, dolar ou real): ").strip().lower()
        valor = input("Valor a ser convertido: ")

        try:
            valor = float(valor)
        except ValueError:
            print("Valor inválido. Digite um número.\n")
            continue

        resultado = conversao(origem, destino, valor)

        if resultado is not None:
            print(f"Convertendo {valor:.2f} {origem} → {destino}")
            print(f"Resultado: {resultado:.2f}")
            break
        else:
            print("Conversão inválida! Verifique as moedas digitadas.\n")



"""
1. Receber dados do usuário
Perguntar qual moeda ele quer converter (moeda de origem), por exemplo: USD, BRL, EUR

Perguntar para qual moeda quer converter (moeda de destino)

Perguntar qual valor deseja converter (ex: 100)

Garantir que o valor digitado é um número positivo (pode ser decimal)

2. Fazer a requisição para a API de câmbio
Usar uma API pública gratuita para pegar a taxa de câmbio atual entre as moedas

Enviar os dados (moeda origem, destino e valor) para a API e receber a resposta com o valor convertido

3. Tratar a resposta da API
Verificar se a API respondeu corretamente (sem erros)

Pegar o valor convertido do JSON retornado pela API

4. Exibir o resultado para o usuário
Mostrar na tela o valor convertido formatado com duas casas decimais
Exemplo: 100.00 USD = 540.25 BRL

5. Tratar erros
Caso a API não responda ou retorne erro, mostrar uma mensagem amigável para o usuário

Caso o usuário digite dados inválidos, avisar e pedir para tentar de novo

"""