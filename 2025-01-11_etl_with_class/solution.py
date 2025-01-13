# import
import json
import csv

# proccessing
# classe responsavel por carregar, transformar e salvar os dados
class DataProccessing():
    def __init__(self, path, extension):
        self.path = path
        self.extension = extension
        self.data = self.load_data()
        self.columns_name = self.get_columns_name()
        self.records_size = self.get_records_size()

    # carrega os dados de acordo com a extensão do arquivo
    def load_data(self):
        if self.extension == 'json':
            return self.load_json()
        elif self.extension == 'csv':
            return self.load_csv()
        # se a extensão for 'list' os dados vieram da função union()
        elif self.extension == 'list':
            data = self.path
            self.path = 'em memoria'
            return data
        else:
            return None

    def load_json(self):
        with open('dados.json', 'r') as file:
            return json.load(file)

    def load_csv(self):
        with open('dados.csv', 'r') as file:
            dados = csv.DictReader(file, delimiter=',')
            return [row for row in dados]

    def get_columns_name(self):
        return list(self.data[0].keys())

    def get_records_size(self):
        return len(self.data)
    
    # renomeia as colunas de acordo com o dicionário passado como parâmetro
    def rename_columns(self, standart_columns_name):
        for dict in self.data:
            for column_name in standart_columns_name:
                    # remove a chave e o valor do dicionário com e re-adiciona com o novo nome da chave
                    dict[standart_columns_name[column_name]] = dict.pop(column_name)
        self.columns_name = self.get_columns_name()
        
    # une dois conjuntos de dados e retorna um novo objeto DataProccessing com extensão 'list'
    def union(a, b):
        data_combined = []
        data_combined.extend(a.data)
        data_combined.extend(b.data)
        return DataProccessing(data_combined, 'list')
    
    # converte a lista de dicionários para uma lista de listas para salvar em um arquivo csv
    def listdict_to_listlist(self):
        listlist = [self.columns_name]
        for dict in self.data:
            temp_list = []
            for value in dict.values():
                temp_list.append(value)
            listlist.append(temp_list)
        return listlist
    
    # salva os dados, de uma lista de dicionários para uma lista de listas, em um arquivo csv
    def save(self, path):
        data = self.listdict_to_listlist()
        
        # " newline='' " é necessário para evitar que uma linha em branco seja adicionada entre as linhas
        with open(path, mode='w', newline='') as file:
            spamwriter = csv.writer(file)
            spamwriter.writerows(data)
            
# input
path_json = 'dados.json'
path_json = 'dados.csv'

# extract
data_json = DataProccessing('data', 'json')
data_csv = DataProccessing('data', 'csv')

# log
print(f'''
## DADOS "JSON" ##
DADOS JSON - NOME DAS COLUNAS: {data_json.columns_name}
QUANTIDADE DE REGISTROS: {data_json.records_size}

## DADOS "CSV" ##
NOME DAS COLUNAS: {data_csv.columns_name}
QUANTIDADE DE REGISTROS: {data_csv.records_size}''')


# transform
standart_columns_name = {
    'codigo': 'id', 'nome_completo': 'nome', 'anos': 'idade'}
data_csv.rename_columns(standart_columns_name)
data_combined = DataProccessing.union(data_csv, data_json)

# log
print(f'''
NOVO NOME DAS COLUNAS DOS DADOS "CSV": {data_csv.columns_name}''')
print(f'''
QUANTIDADE DE REGISTROS DOS DADOS COMBINADOS: {data_combined.get_records_size()}''')


# load
data_combined_path = 'dados_combinados.csv'
data_combined.save(data_combined_path)