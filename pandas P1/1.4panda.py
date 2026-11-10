#查看整個dataframe狀態

import pandas as pd

sales = [
    {"product": "電視", "category": "家電", "price": 30000, "quantity": 2},
    {"product": "冰箱", "category": "家電", "price": 25000, "quantity": 1},
    {"product": "滑鼠", "category": "3C", "price": 800, "quantity": 5},
    {"product": "鍵盤", "category": "3C", "price": 1500, "quantity": 3},
    {"product": "洗衣機", "category": "家電", "price": 18000, "quantity": 2},
    {"product": "耳機", "category": "3C", "price": None, "quantity": 4},
    {"product": "螢幕", "category": "3C", "price": 6500, "quantity": 2},
    {"product": "冷氣", "category": "家電", "price": 42000, "quantity": 1},
]

df = pd.DataFrame(sales)

# print(df.head(3))
# print(df.tail(3))

# df.info()查看data狀態 
# print(df.describe(include="all")) 描述性狀態
# print(df.sample(3)) 隨機取樣
# print(df.sample(8,random_state=42)) #固定隨機值
#print(df.isna().sum())
print(df.dtypes) 
print(df.info())