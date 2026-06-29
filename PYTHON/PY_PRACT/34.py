import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# i. First 8 rows
print("Q34 i) First 8 rows:\n", df.head(8))

# ii. Column names
print("ii) Column names:", df.columns.tolist())

# iii. Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only = True))
print("iii) Missing values filled with mean")

# iv. Remove rows with missing values
df_dropped = df.dropna()
print("iv) Rows with missing values removed")

# v. Group by species
grouped = df.groupby("species")
print("v) Groups:", list(grouped.groups.keys()))

# vi. Mean, Min, Max of sepal_length
print("vi) Sepal Length Mean:", df["sepal_length"].mean())
print("Sepal Length Min:", df["sepal_length"].min())
print("Sepal Length Max:", df["sepal_length"].max())
