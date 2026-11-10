import pandas as pd

products = [
    {"name": "電視", "category": "家電", "price": 30000, "stock": 5},
    {"name": "冰箱", "category": "家電", "price": 25000, "stock": 3},
    {"name": "滑鼠", "category": "3C", "price": 800, "stock": 20},
    {"name": "鍵盤", "category": "3C", "price": 1500, "stock": 15},
    {"name": "洗衣機", "category": "家電", "price": 18000, "stock": 8},
    {"name": "耳機", "category": "3C", "price": None, "stock": 12},
    {"name": "螢幕", "category": "3C", "price": 6500, "stock": 10},
    {"name": "冷氣", "category": "家電", "price": 42000, "stock": 2}
]
df = pd.DataFrame(products)

"""
1.
建立 DataFrame
資料建立
將 products 轉成 DataFrame，並存入變數 df。
"""
# df = pd.DataFrame(products)

"""
2.
Series 與 DataFrame
資料結構
寫兩行程式。第一行：取得 price 欄位，存入 price_series，結果必須是 Series。
第二行：取得 name、stock 兩個欄位，存入 product_df，結果必須是 DataFrame。
"""
#df = pd.DataFrame(products)
#price_series = df["price"]
#product_df = df[["name", "stock"]]

"""
3.
資料規模與維度
資料結構
寫三行程式，分別印出 df 的資料列數、欄位數，以及 price_series 的維度數量。每一行只印出對應的整數。
"""
#print(df.shape[0])
#print(df.shape[1])
#print(price_series.ndim)

"""
4.
索引與欄位
資料結構
寫三行程式，分別印出 df 的索引、所有欄位名稱，以及不包含索引和欄位名稱的資料值陣列。
"""
#print(df.index)
#print(df.columns)
#print(df.values)

"""
5
查看頭尾資料
資料檢視
寫兩行程式，分別印出 df 的前 3 筆資料及最後 2 筆資料。
"""
#print(df.head(3))
#print(df.tail(2))

"""
6
型別與整體資訊
資料檢視
寫兩行程式。第一行：顯示每個欄位的資料型別。第二行：顯示整張表格的非空值數量、資料型別及整體資訊，不要額外印出 None。
"""
#print(df.dtypes)
#df.info()


"""
7
描述性統計
統計與品質
寫兩行程式。第一行：印出數值欄位的基本統計資訊。第二行：印出包含文字與數值欄位的描述性統計資訊。
"""
#df.info()   ## print(df.describe())
#print(df.describe()) 
print(df.describe(include="all"))

"""
8
缺失值與隨機抽樣
統計與品質
寫兩行程式。第一行：印出每個欄位的缺失值數量。第二行：隨機抽取 3 筆資料，固定 random_state=20，並印出結果。
#print(df.isna().sum())
"""
#print(df.isna().sum())
#print(df.sample(3, random_state=20))

"""
9
讀取 CSV 與 Excel
檔案讀寫
假設目前工作目錄有 sales.csv 與 report.xlsx。
寫兩行程式：將 CSV 讀成 sales_df；將 Excel 中名為「2026報表」的工作表讀成 report_df。只需寫程式，不必真的有這些檔案。
"""
#sales_df = pd.read_csv("sales.csv") 
#report_df = pd.read_excel("report.xlsx", sheet_name="2026報表")

"""
10
綜合應用
資料建立與輸出
先建立一個 Dict，變數叫 data，包含兩個 Key：「product」對應 ["電視", "冰箱"]，「price」對應 [30000, 25000]。
將它轉成 DataFrame，存入 new_df，再輸出成 products_result.csv，不要把 Index 寫入 CSV。
"""
#data ={"product": ["冰箱", "電視"], "price": [30000, 25000]}
#new_df = pd.DataFrame(data)
#new_df = new_df.to_csv("products_result.csv", index=False) 

###data ={"product": ["電視", "冰箱"], "price": [30000, 25000]}
###new_df = pd.DataFrame(data)
###new_df.to_csv("products_result.csv", index=False) 