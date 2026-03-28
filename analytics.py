import pandas as pd

df = pd.read_csv("data_preprocessed.csv")

avg_age = df['Age'].mean()
max_income = df['Annual Income (k$)'].max()
avg_score = df['Spending Score (1-100)'].mean()

with open("insight1.txt", "w") as f:
    f.write(f"Average age: {avg_age}")

with open("insight2.txt", "w") as f:
    f.write(f"Max income: {max_income}")

with open("insight3.txt", "w") as f:
    f.write(f"Average spending score: {avg_score}")

print("Insights generated")

import visualize