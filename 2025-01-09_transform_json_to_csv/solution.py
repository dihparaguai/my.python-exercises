import json
import csv

# leitura
path_json = '2025-01-09/produtos.json'

with open(path_json, 'r') as file:
    dados_json = []
    dados_json = json.load(file)


# cabeçalho csv
dados_csv = [list(dados_json[0].keys())]

# criando csv
for row in dados_json:
    list_temp = []
    for column, value in row.items():
        list_temp.append(value)
    dados_csv.append(list_temp)

# salvando csv
with open('2025-01-09/produtos.csv', 'w') as file:
    spamwriter = csv.writer(file)
    spamwriter.writerows(dados_csv)
