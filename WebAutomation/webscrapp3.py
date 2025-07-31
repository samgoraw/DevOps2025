import requests
from bs4 import BeautifulSoup
import pandas as pd


url='https://books.toscrape.com/'

response=requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

books = soup.find_all("article",class_="product_pod")

book_list = [] 

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating_class = book.find("p", class_="star-rating")["class"]
    rating = rating_class[1] if len(rating_class)>1 else "Not Rated"
    link = book.h3.a["href"]

    book_list.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Link": link
        })

    df = pd.DataFrame(book_list)

    print(df)