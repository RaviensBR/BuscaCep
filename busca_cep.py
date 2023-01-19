import requests

def buscaCep():
    while True:
        try:
            cep = input('Digite os 8 numeros do CEP: ')
            if cep.isnumeric() and len(cep) == 8:  # é um "número" de 8 dígitos
                break  # sai do loop
            print('O número deve ter 8 dígitos')
        except ValueError:
            print('Não foi digitado um número')

    while True:
        try:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            requisicao.raise_for_status()
            dados = requisicao.json()
            cep = dados['cep']
            logradouro = dados['logradouro']
            complemento = dados["complemento"]
            bairro = dados['bairro']
            localidade = dados['localidade']
            uf = dados['uf']
            print('Voce buscou pelo CEP', cep)
            print('Endereço completo:', logradouro, complemento)
            print('Bairro:', bairro)
            print('Localidade:', localidade)
            print('UF:', uf)
            break
        except requests.exceptions.HTTPError as errh:
            print ("HTTP Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except KeyError:
            print('CEP INVALIDO')
        except requests.exceptions.RequestException as err:
            print ("Something Else:",err)
        cep = input('Digite os 8 numeros do CEP novamente: ')

print(buscaCep())
