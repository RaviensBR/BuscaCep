import requests
cep = input('Digite seu Cep ' )
link = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(link)
dados = requisicao.json()
cep = dados['cep']
logradouro = dados['logradouro']
complemento = dados["complemento"]
bairro = dados['bairro']
localidade = dados['localidade']
uf = dados['uf']
print('Voce buscou pelo CEP',cep,'Com Bairro:',bairro, 'no Logradouro ',logradouro, complemento, uf )
