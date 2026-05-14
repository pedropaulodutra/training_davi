import requests

pais = input('escreva o nome de um pais')
response = requests.get(f'https://restcountries.com/v3.1/name/{pais.lower()}')
country = response.json()[0]
capital = country['capital'][0]
print('a capital do {} e {}'.format(pais.capitalize(),capital))
