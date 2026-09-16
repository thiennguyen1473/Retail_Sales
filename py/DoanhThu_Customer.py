import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\DoanhThu_customer.csv")

plt.figure(figsize=(10, 6))
plt.barh(df["customer name"], df["tong"], height = 0.6, color='steelblue')

plt.xlabel("Doanh Thu")
plt.ylabel("Khách hàng")
plt.title("Top 10 Doanh thu khách hàng")
plt.gca().invert_yaxis()

plt.legend()
plt.show()