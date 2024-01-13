import pandas as pd
df = pd.read_csv("juyo-d1-j.csv",  encoding="Shift_JIS", skiprows=54, nrows=235-56+1, usecols=[0,1,2], parse_dates=["DATE"])
print(df.tail())