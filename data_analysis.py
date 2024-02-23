import os
import pandas as pd
import matplotlib.pyplot as plt

# Variavel para armazernar o caminho para os dados utilizados na análise
caminho_dados = rf'{os.environ.get("DATA_PATH")}'
print(caminho_dados)
# # Dados 
# ictícios de vendas mensais
dado = pd.read_csv(caminho_dados, sep = ',', encoding='UTF-8')
print(dado)
meses = (dado['Meses'])
vendas_produto_a = (dado['vendas_produto_a'])
vendas_produto_b = (dado['vendas_produto_b'])

# Criando um DataFrame com os dados
df = pd.DataFrame({
    'Mês': meses,
    'Vendas Produto A': vendas_produto_a, 
    'Vendas Produto B': vendas_produto_b
})

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['Mês'], df['Vendas Produto A'], label='Produto A', color='b', alpha=0.7)
plt.bar(df['Mês'], df['Vendas Produto B'], label='Produto B', color='g', alpha=0.7)
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas Mensais de Produtos')
plt.legend()
plt.grid(axis='y')
plt.show()
