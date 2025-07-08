import pandas as pd
import numpy as np

df = pd.read_csv("online_store_data.csv")


df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce").astype("Int32")
df["num_of_ratings"] = pd.to_numeric(df["num_of_ratings"], errors="coerce").astype("Int32")
df["quantity_in_stock"] = pd.to_numeric(df["quantity_in_stock"], errors="coerce").astype("Int32")
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

df["rating"] = df["rating"].apply(lambda x: float(str(x).split()[0]) if pd.notnull(x) and str(x).split()[0].replace('.', '', 1).isdigit() else None)

df = df.dropna(subset=["product_name"])

df = df.dropna(thresh=df.shape[1] - 4)

df = df.drop_duplicates(keep="first")



df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["revenue"] = df["quantity_sold"] * df["price"]


top_keyboards = (
    df[df["category"] == "Keyboards"]
    .sort_values(by="revenue", ascending=False)
    .head(10)
)

bottom_tvs = (
    df[df["category"] == "TVs"]
    .sort_values(by="revenue", ascending=True)
    .head(10)
)

print("\nTop 10 Keyboards po prihodu:\n")
print(top_keyboards[["product_name", "category", "revenue"]])

print("\nBottom 10 TVs po prihodu:\n")
print(bottom_tvs[["product_name", "category", "revenue"]])

top_keyboards.to_csv("top_10_keyboards.csv", index=False)
bottom_tvs.to_csv("bottom_10_tvs.csv", index=False)
