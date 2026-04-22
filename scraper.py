import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"

# QUOTES SCRAPING

quotes = []
authors_dict = {}

url = "/page/1/"

while url:
    response = requests.get(BASE_URL + url)
    soup = BeautifulSoup(response.text, "lxml")

    quote_blocks = soup.find_all("div", class_="quote")

    for q in quote_blocks:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = [t.text for t in q.find_all("a", class_="tag")]

        quotes.append({
            "tags": tags,
            "author": author,
            "quote": text
        })

        # щоб не дублювати авторів
        if author not in authors_dict:
            authors_link = q.find("a")["href"]
            authors_dict[author] = BASE_URL + authors_link

    next_btn = soup.find("li", class_="next")
    url = next_btn.find("a")["href"] if next_btn else None


# AUTHORS SCRAPING

authors = []

for author, link in authors_dict.items():
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "lxml")

    fullname = soup.find("h3", class_="author-title").text.strip()
    born_date = soup.find("span", class_="author-born-date").text.strip()
    born_location = soup.find("span", class_="author-born-location").text.strip()
    description = soup.find("div", class_="author-description").text.strip()

    authors.append({
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description
    })

# SAVE JSON

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(authors, f, ensure_ascii=False, indent=2)



# quotes = soup.find_all("div", class_="quote")

# result = []

# for q in quotes:
#     text = q.find("span", class_="text").text
#     author = q.find("small", class_="author").text
#     tags = [t.text for t in q.find_all("a", class_="tag")]

#     result.append({
#         "tags": tags,
#         "author": author,
#         "quote": text
#     })

# for r in result:
#     print(r)

# poetry run python scraper.py