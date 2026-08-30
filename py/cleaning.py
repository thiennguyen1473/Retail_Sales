import numpy as np
import pandas as pd

calendar = pd.read_csv(r"D:\kaggle\dim_Calendar.csv"
                 )
customer = pd.read_csv(r"D:\kaggle\dim_Customer.csv")

category = pd.read_csv(r"D:\kaggle\dim_Category.csv")

cusSm = pd.read_csv(r"D:\kaggle\dim_CustomerSegment.csv")

Location = pd.read_csv(r"D:\kaggle\dim_Location.csv")

product = pd.read_csv(r"D:\kaggle\dim_Product.csv")

Rsp = pd.read_csv(r"D:\kaggle\dim_RetailSalesPeople.csv")

shipMode = pd.read_csv(r"D:\kaggle\dim_ShipMode.csv")

SubCate = pd.read_csv(r"D:\kaggle\dim_Sub-Category.csv")

factRetaild = pd.read_csv(r"D:\kaggle\fact_RetailOrder.csv")


dfs = {
    "calendar": calendar,
    "customer": customer,
    "category": category,
    "cusSm": cusSm,
    "Location": Location,
    "product": product,
    "Rsp": Rsp,
    "shipMode": shipMode,
    "SubCate": SubCate,
    "factRetaild": factRetaild
}

for x, y in dfs.items():
    print(x,y.columns)
    print("\n")

for x, y in dfs.items():
    col_name = []
    for z in y.columns:
        z = z.strip()
        if z.endswith("ID"):
            z = z.replace("ID", "Id")

        col_name.append(z)
    y.columns = col_name

for x, y in dfs.items():
    for z in y.columns:
        if "Date" in z:
            y[z] = pd.to_datetime(y[z], errors = "coerce")

# factRetaild["Order Date"] = pd.to_datetime(factRetaild["Order Date"])
# factRetaild["Order Date"] = factRetaild["Order Date"].dt.strftime("%y%m%d")

# factRetaild["Ship Date"] = pd.to_datetime(factRetaild["Ship Date"])
# factRetaild["Ship Date"] = factRetaild["Ship Date"].dt.strftime("%y%m%d")
for x, y in dfs.items():
    print(y.isnull().sum())
    print("\n")

for x, y in dfs.items():
    print(x + ":", y.duplicated().sum())


primary_keys = {
   "customer": "Customer Id",
   "category": "Category Id",
    "cusSm":  "CusSegment Id" ,
    "Location": "Postal Code",
    "product": "Product Id",
    "Rsp": "Retail Sales People Id",
    "shipMode": "Ship Mode Id",
    "SubCate": "Sub-Category Id",
    "factRetaild": "Retail Order Id",
    "calendar": "Date"
}

for x, y in dfs.items():
    if x in primary_keys:
        key = primary_keys[x]
        duplicate_cnt = y[key].duplicated().sum()
    print(duplicate_cnt)
#không bị trùng PK

    
print(str(factRetaild["Quantity"].min()) + "\n" + str(factRetaild["Cost"].min()) + "\n" + str(factRetaild["Days"].min()))

# #không có giá trị min nào là âm


# for x, y in dfs.items():
#     y.to_csv(r"D:\kaggle\cleaned_" + x + ".csv", index=False)

#print(dfs["factRetaild"][["Order Date", "Ship Date"]].head(10))
# #dfs["calendar"].to_csv(
#      #r"D:\kaggle\cleaned _" + "calendar" + ".csv", index=False)
dfs["factRetaild"].to_csv(r"D:\kaggle\cleaned_" + "factRetaild" + ".csv", index=False)