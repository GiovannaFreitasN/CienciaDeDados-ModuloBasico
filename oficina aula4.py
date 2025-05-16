import numpy as np
import pandas as pd
#1-Use a lista de números: [12, 45, 67, 23, 89, 34, 22, 90, 56, 78].
numeros = [12, 45, 67, 23, 89, 34, 22, 90, 56, 78]
#2-Calcule a média dos números usando a biblioteca numpy.
media = np.mean(numeros)
print(f"Média: {media}")
#3-Identifique os números que são maiores que a média.
numeros_maiores = [num for num in numeros if num > media]
print(f"Números maiores que a média: {numeros_maiores}")
#4-Armazene os números maiores que a média em um DataFrame do pandas.
df = pd.DataFrame(numeros_maiores, columns=["Numeros Maiores que a Media"])
#5-Salve o DataFrame em um arquivo CSV chamado "numeros_maiores_que_media.csv"
df.to_csv("numeros_maiores_que_media.csv", index=False)
