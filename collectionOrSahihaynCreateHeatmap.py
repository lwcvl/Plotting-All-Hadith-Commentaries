import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

df = pd.read_csv('lifespan40Sahihayn.csv')

heatmapData = pd.pivot_table(df, values='commentators', index=['matn'], columns='year')
plt.figure(figsize = (20, 5))

plot = sns.heatmap(heatmapData, cmap='RdPu', xticklabels=100, yticklabels=False)

plt.xlabel("Year in AH")
plt.ylabel("Sahih Muslim                  Sahih Bukhari", verticalalignment='center')
plt.title("When did they write commentaries on the Sahihayn?")

fig = plot.get_figure()
fig.savefig('HeatMapCommentatorsSahihayn40Floruit.svg')