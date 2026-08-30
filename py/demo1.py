import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\kaggle\query_sql\factretaild.csv")
plt.figure(figsize = (10, 6))

plt.scatter(df["sales"], df["profit"], alpha=0.5,s= 20)
plt.xlabel("x", color = "blue")
plt.ylabel("y", color = "red")
plt.tight_layout()

plt.show()