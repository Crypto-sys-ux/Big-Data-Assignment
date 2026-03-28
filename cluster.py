import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("data_preprocessed.csv")

features = df[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(features)

counts = df['Cluster'].value_counts()

with open("clusters.txt", "w") as f:
    for cluster, count in counts.items():
        f.write(f"Cluster {cluster}: {count} customers\n")

print("Clustering done")