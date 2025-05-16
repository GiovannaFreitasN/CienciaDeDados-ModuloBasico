import pandas as pd
import matplotlib.pyplot as plt

# 1 - identificação e transformação dos dados
df_alunosT1 = pd.DataFrame({
    'id_alunos' : ['maria','joao','pedro','paula'],
    'notas' : [6, 7, 'C', 'A']
})
df_alunosT3 = pd.DataFrame({
    'id_alunos' : ['jose','carlos','ana','joana'],
    'notas' : [10, 9, 'B', 'C']
})
df_alunosT2 = pd.DataFrame({
    'id_alunos' : ['julia','clara','chico','mario'],
    'notas' : [5, 6, 'A', 'A']
})

#dicionario de mapeamento
mapa_notas = {
    'A' : 10,
    'B' : 8,
    'C' : 7
}
# 2 - Padronização dos dados

df_alunosT1['notas_normalizadas'] = df_alunosT1['notas'].replace(mapa_notas)
df_alunosT2['notas_normalizadas'] = df_alunosT2['notas'].replace(mapa_notas)
df_alunosT3['notas_normalizadas'] = df_alunosT3['notas'].replace(mapa_notas)

# 3 - Combinação dos conjuntos de dados

df_todas_turmas = pd.concat([df_alunosT1, df_alunosT2, df_alunosT3], ignore_index=True)
print(df_todas_turmas)

# 4 - Análise e visualização dos dados

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df_todas_turmas['id_alunos'], df_todas_turmas['notas_normalizadas'], color='red')
ax.set_xlabel('id_aluno')
ax.set_ylabel('notas normalizadas')
ax.set_title('notas normalizadas por aluno')

plt.show()