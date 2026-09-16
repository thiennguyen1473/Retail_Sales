import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\DoanhThu_Month.csv")
plt.figure(figsize=(14, 6))
for x in df["year"].unique():
    df_year = df[df["year"] == x]
    plt.plot(
        df_year["month"],
        df_year["tong_month"],
        marker="o",
        label = str(x))

plt.xticks(range(1, 13))

plt.grid(True, alpha=0.3)

plt.legend(
    title="Năm",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()




# plt.figure(figsize=(10, 4))

# df["year-month"] = df["year"].astype(str) + "-" + df["month"].astype(str)
# plt.plot(df["year-month"], df["tong_month"], color = "red")
# plt.xticks(
#     range(0, len(df), 3),
#     df["year-month"].iloc[::3],
#     rotation=45
# )
# plt.tight_layout()
# plt.xlabel("thoi gian")
# plt.xlabel("doanh thu ban duoc theo thang")
# plt.legend()
# plt.show()