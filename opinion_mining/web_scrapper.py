import requests
import csv
import os
import pandas as pd

from bs4 import BeautifulSoup
from langdetect import detect

reviews = []
n_pages = 10
script_dir = os.path.dirname(__file__)
save_dir = os.path.join(script_dir, "data/reviews.csv")
urls_dir = os.path.join(script_dir, "data/coursera_courses.csv")

def get_courses():
    URLs = []
    courses_df = pd.read_csv(urls_dir, skiprows=1, names=["Name", "Instituition", "URL", "ID"])
    courses_urls = courses_df["URL"]

    for url in courses_urls:
        url = url + '/reviews?'
        URLs.append(url)

    return set(URLs)

URLs = get_courses()

polarity = {
    "1": "negative",
    "2": "negative",
    "3": "neutral",
    "4": "positive",
    "5": "positive",
}

for URL in URLs:
    for n_star in range(1, 6):
        for n_page in range(1, n_pages):
            try:
                page = requests.get(URL + "star=" + str(n_star) + "&page=" + str(n_page))
                soup = BeautifulSoup(page.content, "html.parser")
                results = list(soup.find_all("div", attrs={"class": "review"}))

                for result in results:
                    rev_wrap = result.contents[0]
                    rev_text = rev_wrap.find_all("div", attrs={"class": "reviewText"})[
                        0
                    ].text
                    try:
                        language = detect(rev_text)
                        if language == "en":
                            review = [rev_text, n_star, polarity[str(n_star)]]
                            reviews.append(review)
                    except:
                        pass
            except:
                continue

with open(save_dir, "w", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(reviews)
