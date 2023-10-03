import numpy as np
import pandas as pd

oil=pd.read_csv("../retail/oil.csv").dropna()
#print(oil)
oil_array=np.array(oil["dcoilwtico"].iloc[1000:1100])
#print(oil_array)
oil_series=pd.Series(oil_array,name="oil_prices")
print(oil_series)
print(f"Index: {oil_series.index}, Size: {oil_series.size}")
oil_series=oil_series.astype(int)

dates=np.array(oil["date"].iloc[1000:1100])
oil_series.index=dates
print(oil_series)

#mean of first and last 10 values
print("Mean of first 10 ",oil_series.iloc[:10].mean())
print("Mean of last 10 ",oil_series.iloc[:-10].mean())

oil_series.loc["2017-01-01":"2017-01-07"].reset_index(drop=True)

# lowest 10 price
print(oil_series.sort_values().iloc[:10])
