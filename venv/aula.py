while True:
    try:
        cep = input('Digite os 8 numeros do CEP: ')
        if cep.isnumeric() and len(cep) == 3: # é um "número" de 3 dígitos
            break # sai do loop
        print('O número deve ter 8 dígitos')
    except ValueError:
        print('Não foi digitado um número')

print(cep[::-1]) # imprime invertido

link = f'https://viacep.com.br/ws/{cep}/json/'
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
