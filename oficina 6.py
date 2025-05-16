import numpy as np
import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [28, 34, 29, None, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', None, 'Curitiba', 'Belo Horizonte'],
    'Vendas': [150, 200, 300, 400, None]
}

# 1 - Crie um DataFrame com base nos dados fornecidos;
df = pd.DataFrame(dados)
print(df)
# 2 - Filtre os clientes que têm mais de 30 anos
maiorQue30 = df[df['Idade'] >= 30]
print(maiorQue30)
# 3 - Calcule a média de idade dos clientes
mediaDaIdade = df['Idade'].mean()
print(f"Média das idades: {mediaDaIdade}")
# 4 - Substitua valores faltantes na coluna Cidade por ‘Desconhecido’
df['Idade'] = df['Idade'].fillna('Desconhecido')
print(df)
# 5 - Calcule a soma das vendas
somaVendas = np.sum('Vendas')
print(somaVendas)