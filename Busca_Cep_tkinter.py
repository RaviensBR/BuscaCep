import tkinter as tk
import requests


def busca_cep(event=None):
    cep = entry.get()
    if len(cep) != 8 or not cep.isnumeric():
        result_label.config(text="O CEP deve conter 8 dígitos e ser numérico.")
        return
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 404:
            result_label.config(text="CEP não encontrado.")
            return
        response.raise_for_status()
        dados = response.json()
        logradouro = dados.get("logradouro", "")
        complemento = dados.get("complemento", "")
        bairro = dados.get("bairro", "")
        localidade = dados.get("localidade", "")
        uf = dados.get("uf", "")
        cep = dados.get("cep", "")

        cep_frame = tk.Frame(root, bd=1, relief="solid")
        cep_frame.place(x=30, y=80)

        cep_box = tk.Label(cep_frame, text="CEP: "+cep, font=("Arial", 12))
        cep_box.pack()

        endereco_frame = tk.Frame(root, bd=1, relief="solid")
        endereco_frame.place(x=30, y=110)

        endereco_box = tk.Label(
            endereco_frame, text="Endereço: "+logradouro+" "+complemento, font=("Arial", 12))
        endereco_box.pack()

        bairro_frame = tk.Frame(root, bd=1, relief="solid")
        bairro_frame.place(x=30, y=140)

        bairro_box = tk.Label(
            bairro_frame, text="Bairro: "+bairro, font=("Arial", 12))
        bairro_box.pack()

        cidade_frame = tk.Frame(root, bd=1, relief="solid")
        cidade_frame.place(x=30, y=170)

        cidade_box = tk.Label(cidade_frame, text="Cidade: " +
                              localidade+"-"+uf, font=("Arial", 12))
        cidade_box.pack()
    except requests.exceptions.HTTPError as e:
        result_label.config(text=f"Erro: {e}")


root = tk.Tk()
root.geometry("400x300")
root.title("Busca de CEP by:                               Claudio Melo")

entry = tk.Entry(root, validate="key", validatecommand=(
    root.register(lambda x: len(x) <= 8), '%P'))
entry.place(x=30, y=30)
entry.bind("<Return>", busca_cep)

buscar_button = tk.Button(
    root, text="Buscar", font=("Arial", 12), command=busca_cep)
buscar_button.place(x=320, y=28)

result_label = tk.Label(root, font=("Arial", 12))
result_label.place(x=30, y=60)

root.mainloop()
