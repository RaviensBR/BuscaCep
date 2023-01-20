import requests
from tkinter import *


def buscaCep():
    cep = entry.get()
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
        resultado_label.config(
            text=f'Endereço completo: {logradouro}, {complemento}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}')
    except requests.exceptions.HTTPError as errh:
        resultado_label.config(text=f'HTTP Error: {errh}')
    except requests.exceptions.ConnectionError as errc:
        resultado_label.config(text=f'Error Connecting: {errc}')
    except requests.exceptions.Timeout as errt:
        resultado_label.config(text=f'Timeout Error: {errt}')
    except KeyError:
        resultado_label.config(text='CEP inválido')


# Create a window
root = Tk()
root.title("Busca CEP")

# Create an input field for the user to enter the CEP
entry = Entry(root)
entry.pack()

# Create a label to display the result
resultado_label = Label(root, text="")
resultado_label.pack()

# Create a button to start the search
buscar_button = Button(root, text="Buscar", command=buscaCep)
buscar_button.pack()

root.mainloop()
