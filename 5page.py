import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books_data = []

# Loop for first 5 pages
for page in range(1, 6):
    print(f"Scraping page {page}...")
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = soup.select('article.product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.select_one('.price_color').text.strip()
        availability = book.select_one('.availability').text.strip()
        relative_url = book.h3.a['href']
        book_url = "http://books.toscrape.com/catalogue/" + relative_url

        books_data.append([title, price, availability, book_url])
    
    time.sleep(1)  # Thoda rukne k liye to be polite

# Save to CSV
with open("5page_data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Availability", "URL"])
    writer.writerows(books_data)

print("✅ Done! Data saved in 'books_data.csv'")
