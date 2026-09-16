import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\DoanhThu_CateProduct.csv")

plt.barh(df["product id"],df["tong"])

plt.xlabel("Doanh thu")
plt.ylabel("Tên sản phẩm")
plt.title("Top 3 doanh thu theo category")
plt.gca().invert_yaxis()
plt.show()