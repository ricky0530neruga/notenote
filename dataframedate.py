import pandas as pd
 

timestep = {
"timestamp": ["2026-03-02 09:05:00", "2026-03-02 09:01:00", "2026-03-02 09:03:00"],
"person": ["worker_B  ", "worker_A ", " worker_A"],
"event": ["enter_zone", "enter_zone", "no_helmet"],
"value": ["1.92  ", "0.95", "0.88  "],
}

df = pd.DataFrame(timestep)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["value"] = df["value"].str.strip().astype(float) #.str.strip() 去空白 僅能用於字串 "" 但不能用於數字 float可以用於兩者
df = df.sort_values("timestamp") #排序 預設小到大



print(df["timestamp"].diff()) #diff 算時間差
print("---")
print(df)
print("---")
print(df.dtypes)





