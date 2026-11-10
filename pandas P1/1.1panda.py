expenses = [
    {"category": "早餐", "amount": 85},
    {"category": "交通", "amount": 120},
    {"category": "晚餐", "amount": 240}
]

df = pd.DataFrame(products)

prices=df["price"]
result = df[["stock", "name"]]