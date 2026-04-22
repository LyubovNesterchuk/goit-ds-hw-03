# 🐱 Kittens MongoDB CRUD (Python + PyMongo)

This project demonstrates basic CRUD operations (Create, Read, Update, Delete) using MongoDB Atlas and Python.
The application manages a collection of kittens stored in MongoDB.

---

## ⚙️ Tech Stack

- Python 3.11
- MongoDB Atlas
- PyMongo
- Poetry
---

## 📦 Installation

Install dependencies:

```bash
poetry add pymongo
```

---

## 🗄️ Database Setup
This project uses MongoDB Atlas (cloud database).
Database: myKittens
Collection: kittens

---

## 📌 Features (CRUD)
🟢 Create
Add new kitten documents to the collection.
🔵 Read
Get all kittens
Find kitten by name
🟡 Update
Update kitten age by name
Add new feature to kitten
🔴 Delete
Delete kitten by name
Delete all kittens

---

## 📁 Project Structure
├── db.py          # MongoDB connection  
└── main.py        # CRUD functions




# 🌐 Quotes Scraper (BeautifulSoup + JSON Export)

This project scrapes data from http://quotes.toscrape.com and saves it into JSON files.

It collects:
- All quotes from all pages
- Unique authors with detailed information

---

## ⚙️ Tech Stack

- Python 3.11
- Requests
- BeautifulSoup4
- lxml
- JSON

---

## 📦 Installation

Install dependencies:

```bash
poetry add requests beautifulsoup4 lxml
```
---

## 🚀 Features

### 📌 Quotes scraping
Scrapes ALL pages of the website
- Extracts:
quote text
author
tags

### 👤 Authors scraping
Extracts unique authors only once
- Collects:
fullname
birth date
birth location
description

---

## 📁 Output files

- quotes.json
[
  {
    "quote": "...",
    "author": "...",
    "tags": ["..."]
  }
]

- authors.json
[
  {
    "fullname": "...",
    "born_date": "...",
    "born_location": "...",
    "description": "..."
  }
]

---

## ▶️ Run scraper

```bash
poetry run python scraper.py
```

---

## ☁️ Optional next step
The generated JSON files can be imported into MongoDB Atlas collections:
quotes
authors

---

## 📁 Project Structure
├── scraper.py           
├── quotes.json 
└── authors.json      