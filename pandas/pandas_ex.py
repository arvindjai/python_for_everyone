import pandas as pd

a = [1, 7, 2]
index = ["x", "y", "z"]
myvar = pd.Series(a, index)

# print(myvar)
print(myvar['y']) # Accessing element by label
print(myvar['x':'y'])
print(myvar.iloc[1]) # Accessing Element by location