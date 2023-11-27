import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('dop2.csv', delimiter=',')

dataframes = []
for date in '10/09/18','10/10/18','08/11/18','10/12/18':
    divided_date_data = data[data['<DATE>'] == date]
    df = pd.DataFrame(divided_date_data, columns=['<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']).assign(Date=date)
    dataframes.append(df)
# Подготовка данных для создания диаграммы
cdf = pd.concat(dataframes)
mdf = pd.melt(cdf, id_vars=['Date'], var_name=['Type'])

ax = sns.boxplot(x='Date', y='value', hue='Type', data=mdf)
# Отображение диаграммы
plt.savefig('dop3.png')
