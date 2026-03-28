import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data_preprocessed.csv")

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True)

plt.subplot(1, 3, 2)
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=df)

plt.subplot(1, 3, 3)
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Visualization done")

import cluster