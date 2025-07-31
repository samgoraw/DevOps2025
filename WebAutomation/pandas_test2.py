import pandas as pd

data = [
    {"Title": "Python 101", "Price": 230.0, "Rating": 5},
    {"Title": "Learn Pandas", "Price": 237.0, "Rating": 4},
    {"Title": "Web Scrapping guide", "Price": 199.0, "Rating": 4},
    {"Title": "Machine Learning Basics", "Price": 340.0, "Rating": 5},
    {"Title": "Data Science Hand Book", "Price": 890.0, "Rating": 3}
]

df = pd.DataFrame(data)
print(df)

high_rated = df[df["Rating"] > 4]
print(high_rated)

sorted_df = df.sort_values(by="Price")
print(sorted_df)
sorted_df = df.sort_values(by="Price",ascending = False)
print(sorted_df)

df["Price_USD"] = df["Price"] * 1.25
print(df)

print("Average Price:",df["Price"].mean())
print("Average Rating:",df["Rating"].mean())

under_threehundred = df[df["Price"] < 300]
under_threehundred.to_csv('underthreehundred.csv',index = False)