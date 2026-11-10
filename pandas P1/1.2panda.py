import pandas as pd

products = [
    {"name": "電視", "price": 30000, "stock": 5},
    {"name": "冰箱", "price": 25000, "stock": 3},
    {"name": "洗衣機", "price": 18000, "stock": 8},
    {"name": "冷氣", "price": 42000, "stock": 2}
]
df = pd.DataFrame(products)

#都是屬性 使用不需要()
""" 
df = pd.DataFrame(products)
df.index	查看資料列索引	Index  
df.columns	查看欄位名稱	Index
df.values	取得資料值	NumPy ndarray
df.shape	查看列數和欄數	Tuple
df.ndim	查看維度數量	整數
df.dtypes	查看各欄型別	Series
"""
# print(df.shape[0], df.shape[1])
print(df.values)

