import pandas as pd
df = pd.DataFrame([
    ["apple", 100, "red"],
    ["kiwi", 200, "brown"],
    ["melon", 800, "green"],
], columns=["fruits", "price", "color"])
print(df)

df2 = pd.DataFrame(
    {
        "fruits": ["apple", "kiwi", "melon"],
        "price": [100, 200, 800],
        "color": ["red", "brown", "green"],
    }
)
print(df2)