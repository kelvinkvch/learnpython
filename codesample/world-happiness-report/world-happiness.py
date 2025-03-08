#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")
#%%
wh = pd.read_csv("2019.csv")
wh.describe()
#%%
# Creates a heat map which displays correlation between each variable
wh1 = wh[['GDP per capita', 'Social support', 'Healthy life expectancy', 
'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']]
cor = wh1.corr()
sns.heatmap(cor, square = True)
#%%
# Create a scatter plot which displays correlation between Social Support and Healthy Life Expectancy
x = wh["GDP per capita"]
y = wh["Healthy life expectancy"]
plt.scatter(x, y)
plt.title("GDP Per Captia Effect on Healthy Life Expectancy")
plt.xlabel("GDP Per Captia")
plt.ylabel("Healthy Life Expectancy")

plt.show()
