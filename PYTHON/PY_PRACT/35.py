import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toyota.csv")   # download from Kaggle and place in working directory

# i. Scatter plot: Age vs Price
plt.figure()
plt.scatter(df["Age"], df["Price"], color = "blue", alpha = 0.5)
plt.title("Age vs Price of Cars")
plt.xlabel("Age (years)")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# ii. Histogram: KM driven
plt.figure()
plt.hist(df["KM"], bins = 20, color = "green", edgecolor = "black")
plt.title("Frequency Distribution of KM Driven")
plt.xlabel("Kilometers Driven")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# iii. Bar plot: Distribution by Fuel Type
fuel_counts = df["FuelType"].value_counts()
plt.figure()
fuel_counts.plot(kind = "bar", color = "orange", edgecolor = "black")
plt.title("Distribution of Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# iv. Pie chart: Percentage distribution by Fuel Type
plt.figure()
fuel_counts.plot(kind = "pie", autopct = "%1.1f%%", startangle = 90)
plt.title("Percentage Distribution by Fuel Type")
plt.ylabel("")
plt.tight_layout()
plt.show()

# v. Box plot: Price across Fuel Types
df.boxplot(column = "Price", by = "FuelType")
plt.title("Price Distribution by Fuel Type")
plt.suptitle("")
plt.xlabel("Fuel Type")
plt.ylabel("Price")
plt.tight_layout()
plt.show()
