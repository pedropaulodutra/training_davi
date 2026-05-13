import requests
cep = '25740100'
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
endereco = response.json()
print(endereco['bairro'])