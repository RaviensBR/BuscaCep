import tkinter as tk
import requests


def busca_cep(event=None):
    cep = entry.get()
    if len(cep) != 8 or not cep.isnumeric():
        result_box.config(state='normal')
        result_box.delete("1.0", tk.END)
        result_box.insert(
            tk.END, "O CEP deve conter 8 dígitos e ser numérico.")
        result_box.config(state='disabled')
        return
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 404:
            result_box.config(state='normal')
            result_box.delete("1.0", tk.END)
            result_box.insert(tk.END, "CEP não encontrado.")
            result_box.config(state='disabled')
            return
        response.raise_for_status()
        dados = response.json()
        logradouro = dados.get("logradouro", "")
        complemento = dados.get("complemento", "")
        bairro = dados.get("bairro", "")
        localidade = dados.get("localidade", "")
        uf = dados.get("uf", "")
        cep = dados.get("cep", "")
        result_box.config(state='normal')
        result_box.delete("1.0", tk.END)
        result_box.insert(
            tk.END, f"CEP: {cep}\nEndereço: {logradouro} {complemento}\nBairro: {bairro}\nCidade: {localidade}-{uf}")
        result_box.config(state='disabled')
    except requests.exceptions.HTTPError as e:
        result_box.config(state='normal')
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "CEP não encontrado.")
        result_box.config(state='disabled')


root = tk.Tk()
root.geometry("350x200")
root.title("Busca de CEP")

label = tk.Label(root, text="Digite o CEP:")
label.pack()

entry = tk.Entry(root, validate="key", validatecommand=(
    root.register(lambda x: len(x) <= 8), '%P'))
entry.pack()
root.bind('<Return>', busca_cep)

button = tk.Button(root, text="Buscar", command=busca_cep)
button.pack()

result_box = tk.Text(root, height=10, width=30)
result_box.pack()
result_box.config(state='disabled')

root.mainloop()
