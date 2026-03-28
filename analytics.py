import pandas as pd

# Use RAW data instead
df = pd.read_csv("data_raw.csv")

avg_age = round(df['Age'].mean())
max_income = int(df['Annual Income (k$)'].max())
avg_score = round(df['Spending Score (1-100)'].mean(), 1)

with open("insight1.txt", "w") as f:
    f.write(f"Average age: {avg_age}")

with open("insight2.txt", "w") as f:
    f.write(f"Max income: {max_income}")

with open("insight3.txt", "w") as f:
    f.write(f"Average spending score: {avg_score}")

print("Insights generated")

import visualize