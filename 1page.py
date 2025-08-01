import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.select('article.product_pod')

books_data = []

for book in books:
    title = book.h3.a['title']
    price = book.select_one('.price_color').text.strip()
    availability = book.select_one('.availability').text.strip()
    relative_url = book.h3.a['href']
    book_url = "http://books.toscrape.com/" + relative_url

    books_data.append([title, price, availability, book_url])

# Save to CSV
with open("page1_data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Availability", "URL"])
    writer.writerows(books_data)

print("✅ Done! Page 1 data saved in 'books_page1.csv'")
