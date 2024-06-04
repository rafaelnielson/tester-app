import pandas as pd

data = pd.read_csv('./data/controle_pacientes_csv.csv')


busca_nome = data['Nome completo:']
input = input('Entre o nome da busca:')
flag = False

for i in busca_nome:
    if i == input:
        flag = True
        break

if flag:
   print(f'Sucesso, nome {input} encontrado!')      
else:
    print('Nome não encontrado!!!!!!!!!')

