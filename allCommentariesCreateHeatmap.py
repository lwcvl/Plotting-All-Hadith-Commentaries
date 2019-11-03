import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

df = pd.read_csv('lifespan40All.csv')

heatmapData = pd.pivot_table(df, values='commentators', index=['all'], columns='year')
plt.figure(figsize = (20, 4))

plot = sns.heatmap(heatmapData, cmap='BuPu', xticklabels=100, yticklabels=False)


plt.xlabel("Year in AH")
plt.ylabel("")
plt.title("Commentaries on the Six Canonical Hadith Collections")

fig = plot.get_figure()
fig.savefig('lifeSpan40allCommentators.svg')