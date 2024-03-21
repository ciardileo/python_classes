""" 
teste de gráficos usando pandas e numpy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Nome_Completo': ['Lancelot Espada', 'Valkyria Frost', 'Maximus Thunder', 'Aria Nightshade', 'Orion Starfall'],
    'Pontuação': [1500, 1800, 1350, 1650, 2000],
    'Idade': [12, 14, 17, 28, 20]
}

df = pd.DataFrame(dados, columns=['Nome_Completo', 'Nome', 'Sobrenome', 'Idade', 'Pontuação'])

df['Pontuação'] = np.random.randint(0, 101, size=5)
df['Nome'] = df.Nome_Completo.str.split().str[0]
df['Sobrenome'] = df.Nome_Completo.str.split().str[1]
df['ID_Nome'] = df.Nome.str[0] + df.Sobrenome.str[0]

df.index = df.ID_Nome
df = df.drop("ID_Nome", axis=1)

print(df)

df.plot(x="Idade", y='Pontuação')
plt.show()