import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\kaggle\query_sql\SalesMonth.csv")
plt.figure(figsize=(10, 4))

df["year-month"] = df["year"].astype(str) + "-" + df["month"].astype(str)
plt.plot(df["year-month"], df["tong_month"], color = "red")
plt.xticks(
    range(0, len(df), 3),
    df["year-month"].iloc[::3],
    rotation=45
)
plt.tight_layout()
plt.xlabel("thoi gian")
plt.xlabel("doanh thu ban duoc theo thang")
plt.legend()
plt.show()