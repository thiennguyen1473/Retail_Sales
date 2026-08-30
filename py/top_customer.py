import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"D:\kaggle\query_sql\top_customer.csv")

# plt.figure(figsize = (12,6))
# plt.bar(df["customer id"], df["sum(f.sales)"])
# plt.xlabel("khách hàng", color = "green", size = 15)
# plt.ylabel("doanh thu", color = "green", size = 15)
# plt.title("top 10 khách hàng có doanh thu cao nhất", color = "black", size = 20)
# plt.show()


plt.figure(figsize=(10, 6))

plt.barh(df["customer name"], df["sum(f.sales)"])

plt.xlabel("Total Sales", size = 15)
plt.ylabel("Customer", size = 15)
plt.title("Top 10 Customers by Sales")

# Khách hàng doanh thu cao nhất nằm trên cùng
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()