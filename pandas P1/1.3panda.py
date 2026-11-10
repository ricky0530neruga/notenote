import pandas as pd

# df = pd.Dataframe()

""" 建立CSV index值不另列入 CSV欄位 
df = pd.DataFrame({
    "name": ["電視", "冰箱", "洗衣機"],
    "price": [30000, 25000, 18000]
})

df.to_csv("products.csv", index=False, encoding="utf-8-sig") 
"""
# new_df = pd.read_csv("products.csv") 讀CSV

# df = pd.read_excel("products.xlsx") 讀excel
#df = pd.read_excel("report.xlsx", sheet_name="2026銷售")
 # 可以直接讀windows路徑 #df = pd.read_csv(r"C:\Users\SCE\Desktop\products.csv") r跳脫 

"""
特性	        CSV	            Excel（XLSX）
Pandas 讀取	  read_csv()	   read_excel()
多張工作表	   不支援	       支援
儲存格式與公式	不支援	       支援
讀取速度	   通常較快	       通常較慢
常見用途	資料交換、程式分析	商業報表、人工維護
"""
    
