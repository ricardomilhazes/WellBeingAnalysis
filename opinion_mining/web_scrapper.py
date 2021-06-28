import requests
import csv
from bs4 import BeautifulSoup
from langdetect import detect

reviews = []
n_pages = 0
URL = "https://pt.coursera.org/learn/machine-learning/reviews?"

polarity = {
    "1": "negative",
    "2": "negative",
    "3": "neutral",
    "4": "positive",
    "5": "positive",
}

for n_star in range(1, 6):

    if n_star == 1:
        n_pages = 5
    elif n_star == 2:
        n_pages = 4
    elif n_star == 3:
        n_pages = 12
    elif n_star == 4:
        n_pages = 105  # 105
    elif n_star == 5:
        n_pages = 400  # 400

    for n_page in range(1, n_pages):
        page = requests.get(URL + "star=" + str(n_star) + "&page=" + str(n_page))
        soup = BeautifulSoup(page.content, "html.parser")
        results = list(soup.find_all("div", attrs={"class": "review"}))

        for result in results:
            rev_wrap = result.contents[0]
            rev_text = rev_wrap.find_all("div", attrs={"class": "reviewText"})[0].text
            if detect(rev_text) == "en":
                review = [rev_text, n_star, polarity[str(n_star)]]
                reviews.append(review)

with open("reviews.csv", "w", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(reviews)
