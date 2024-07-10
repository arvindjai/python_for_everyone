import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 25, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
        'Work':['Engineer','Plumber','Artist','Copy writer']}

df = pd.DataFrame(data)
# print(df)
# print(df['Name']) # Accessing Name column
print(df[['Name', 'Age', 'Work']]) # Accessing multiple column by Column name
print(df[1:3]) # Accessing Row 
# print(df.iloc[3])
# print(df.iloc[1])

unique_date = df['Age'].unique() # unique method
# print(unique_date)

high_above = df[df['Age'] > 25] #conditonal filter in DataFrame
print(high_above)