"""
tipos de gráficos e customizações
"""

import matplotlib.pyplot as plt

x, y = [1, 3, 5], [2, 4, 7]
w, z = [1, 6, 8], [1, 11, 12]

# gráfico de barras
plt.bar(x, y, color='green')
plt.show()

# histograma
plt.hist(x, y, rwidth=1, histtype='bar') # rwidth = row width
plt.show()

# gráfico de dispersão / gráfico de pontos
plt.scatter(x, y, label='gráfico de dispersão', marker='o')  # marker = símbolo do ponto
plt.legend()
plt.show()

# gráfico de área empilhada 

# Anos
anos = [2010, 2012, 2014, 2016, 2018]

# Número de usuários para cada rede social ao longo dos anos
facebook = [500, 700, 1000, 1500, 2000]
instagram = [100, 300, 600, 1200, 1800]
twitter = [200, 400, 800, 1000, 1500]
linkedin = [50, 100, 200, 400, 800]
snapchat = [50, 150, 300, 600, 1000]

plt.figure(figsize=(10, 6))  # Definir o tamanho do gráfico
plt.stackplot(anos, facebook, instagram, twitter, linkedin, snapchat, labels=['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat'])

# Adicionar título e rótulos aos eixos
plt.title('Número de Usuários por Rede Social ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Número de Usuários (em milhões)')

# Adicionar legenda
plt.legend()

# Exibir o gráfico
plt.grid(True)  # Adicionar grade
plt.tight_layout()  # Ajustar layout
plt.show()

# gráfico de pizza

fatias_redes = [2000, 1800, 1500, 800, 1000]
empresas = ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Snapchat']


plt.figure(figsize=(8, 8))
plt.pie(fatias_redes, labels=empresas, shadow=True, explode=(0, 0.2, 0, 0, 0))
plt.title("Usuários (em milhões) de cada Rede Social")
plt.legend()
plt.tight_layout()
plt.show()