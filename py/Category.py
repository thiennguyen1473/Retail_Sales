import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\Doanhthu_Category.csv")

x = range(len(df["category"]))
plt.figure(figsize = (10, 6))
width = 0.2

sales = []

for i in x:
    t = i - width/2
    sales.append(t)

profit = []

for i in x:
    p = i + width/2
    profit.append(p)

plt.bar(sales, df["total_sales"], label = "sales", width = 0.2)

plt.bar(profit, df["total_profit"], label = "profit", width = 0.2)

plt.xlabel("Danh mục sản phẩm")
plt.ylabel("Doanh thu và lợi nhuận")
plt.title("Doanh thu và lợi nhuận theo danh mục sản phẩm")
plt.xticks(x, df["category"])
plt.legend()
plt.show()



                 