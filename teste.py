import requests
def EntradaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um CEP Válido. \033[m')
        if ok:
            break
    return valor

n = EntradaInt('Digite seu Cep: ')
link = f'https://viacep.com.br/ws/{n}/json/'
requisicao = requests.get(link)
dados = requisicao.json()
cep = dados['cep']
logradouro = dados['logradouro']
complemento = dados["complemento"]
bairro = dados['bairro']
localidade = dados['localidade']
uf = dados['uf']
print('Voce buscou pelo CEP', cep, 'Com Bairro:', bairro,
      'no Logradouro ', logradouro, complemento, uf)
