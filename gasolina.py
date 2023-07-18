import pandas as pd
import seaborn as sns

#%%writefile gasolina.csv
#dia,venda
#1,5.11
#2,4.99
#3,5.02
#4,5.21
#5,5.07
#6,5.09
#7,5.13
#8,5.12
#9,4.94
#10,5.03

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

with sns.axes_style ('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico_gasolina.set(title='Gasolina em São Paulo/SP nos 10 primeiros dias de Julho de 2021', xlabel='Dia', ylabel='Preço')
  grafico_gasolina.get_figure().savefig(f"gasolina.png")