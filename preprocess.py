import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("data_raw.csv")

print("Original shape:", df.shape)

df = df.dropna()
df = df.drop_duplicates()

df['Age Group'] = pd.cut(df['Age'], bins=3, labels=['Young', 'Middle', 'Old'])

le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

scaler = StandardScaler()
cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
df[cols] = scaler.fit_transform(df[cols])

pca = PCA(n_components=2)
pca_values = pca.fit_transform(df[cols])

df['PCA1'] = pca_values[:, 0]
df['PCA2'] = pca_values[:, 1]


df.to_csv("data_preprocessed.csv", index=False)

print("Preprocessing done")

import analytics