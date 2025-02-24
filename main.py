"""Main function of the script. 
Have different functions to load the info from the webpage and 
how to work with the files"""

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_list_from_web(page_id):
    """Function to get the all the articles from the page."""
    # initialize an empty list to store the article information
    page_article_list = []
    # Initialize a variable to store the URL of the article
    article_url = ""
    url = "https://www.todoconsolas.com/197-manga?order=product.name.asc&page=" + \
        str(page_id)
    # retrieve the HTML content of the page using the requests module
    page = requests.get(url, timeout=100)
    # parse the HTML content using the BeautifulSoup library
    soup = BeautifulSoup(page.content, "html.parser")
    # find all the product info sections on the page
    results = soup.find_all("div", {"class": "product-info"})
    # loop through each product info section and extract the title, price, and URL
    for job_element in results:
        # find the product title and price within the current section
        title = job_element.find("h2", class_="h3 product-title")
        price = job_element.find("span", class_="price")
        # find all the links within the current section
        a_tags = job_element.find_all("a", href=True)
        # loop through each link and check if it is not a placeholder link
        for tag in a_tags:
            if tag["href"] != "#":
                # store the URL of the article
                article_url = tag["href"]
        # create a dictionary to store the article information
        article = [title.text, price.text, article_url]
        # add the dictionary to the page_article_list
        page_article_list.append(article)
    # return the page_article_list
    return page_article_list


def get_last_page_number():
    """Function to get the last page from the website"""
    web_page_numbers = []
    url = "https://www.todoconsolas.com/es/197-manga?order=product.name.asc&page=1"
    page = requests.get(url, timeout=100)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(
        "ul", {"class": "page-list clearfix text-sm-center"})
    for job_element in results:
        numbers = job_element.find_all("a", class_="js-search-link")
        for number in numbers:
            if number.text.strip().isnumeric():
                web_page_numbers.append(int(number.text.strip()))
    web_page_numbers.sort()
    return web_page_numbers[-1]


def transform_file():
    """Function to rename the current file before creating a new one"""

    if os.path.isfile("yesterday.csv"):
        os.remove("yesterday.csv")
    if os.path.isfile("today.csv"):
        os.rename("today.csv", "yesterday.csv")


def page_info_to_csv():
    """Function to loop for all thew pages in the website, store in a DF, and save to csv"""
    article_list = []
    for x in range(get_last_page_number()):
        article_list.extend(get_list_from_web(x))
    df = pd.DataFrame(article_list, columns=["Name", "price", "URL"])
    df[["type", "Name"]] = df["Name"].str.split(n=1, expand=True)
    df["price"] = df["price"].str.extract(r"(\d+,\d{2})")
    df["price"] = df["price"].str.replace(",", ".")
    df["price"] = df["price"].astype(float)
    df.to_csv("today.csv", sep=";", index=False)


if __name__ == "__main__":
    transform_file()
    page_info_to_csv()
