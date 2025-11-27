import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample-data.csv")

income_by_year = df.groupby("year")["income"].mean()

plt.plot(income_by_year.index, income_by_year.values, marker="o")
plt.title("Average Household Income Over Time")
plt.xlabel("Year")
plt.ylabel("Income")
plt.grid(True)
plt.show()
