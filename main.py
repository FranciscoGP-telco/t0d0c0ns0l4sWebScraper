"""Main function of the script. 
Have different functions to load the info from the webpage and 
how to work with the files"""

import os
from typing import List
import logging
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Constants
CURRENT_FILE = "current.csv"
PREVIOUS_FILE = "previous.csv"
URL = "https://www.todoconsolas.com/197-manga?order=product.name.asc&page="

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_list_from_web(page_id: int) -> List[List[str]]:
    """
    Fetches a list of articles from the specified page of the website.

    Args:
        page_id (int): The page number to fetch articles from.

    Returns:
        Optional[List[List[str]]]: 
        A list of articles, where each article is represented as a list of strings.
        Returns None if there is an error in the request.
    """
    page_article_list = []
    article_url = ""
    url = f"{URL}{str(page_id)}"

    try:
        page = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        logging.error("Error in request: %s", e)
        return None

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", {"class": "product-info"})

    for job_element in results:
        title = job_element.find("h2", class_="h3 product-title")
        price = job_element.find("span", class_="price")
        a_tags = job_element.find_all("a", href=True)
        for tag in a_tags:
            if tag["href"] != "#":
                article_url = tag["href"]

        article = [title.text, price.text, article_url]
        page_article_list.append(article)
    return page_article_list


def transform_file() -> None:
    """
    Renames the current file to the previous file before creating a new one.
    If the previous file exists, it is removed.
    """
    if os.path.isfile(PREVIOUS_FILE):
        os.remove(PREVIOUS_FILE)
    if os.path.isfile(CURRENT_FILE):
        os.rename(CURRENT_FILE, PREVIOUS_FILE)


def page_info_to_csv() -> None:
    """
    Fetches articles from all pages of the website, 
    stores them in a DataFrame, and saves the DataFrame to a CSV file.
    """
    article_list = []
    page_num = 1
    while True:
        current_articles_list = get_list_from_web(page_num)
        if not current_articles_list:
            break
        article_list.extend(current_articles_list)
        page_num += 1

    df = pd.DataFrame(article_list, columns=["Name", "price", "URL"])
    if df.empty:
        logging.error("No articles found.")
        return
    df[["type", "Name"]] = df["Name"].str.split(n=1, expand=True)
    df["price"] = df["price"].str.extract(r"(\d+,\d{2})")
    df["price"] = df["price"].str.replace(",", ".")
    df["price"] = df["price"].astype(float)
    df.to_csv(CURRENT_FILE, sep=";", index=False)


if __name__ == "__main__":
    transform_file()
    page_info_to_csv()
