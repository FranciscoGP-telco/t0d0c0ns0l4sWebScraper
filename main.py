import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

#Class with the logic about the telegram Bot
class telegramBot():
    def __init__(self, token, chatId):
        self.token = token
        self.chatId = chatId
    
    def getMessages(self):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        results = requests.get(url).json()
        for result in results['result']:
            username = result['message']['from']['username']
            message = result['message']['text']
            print(f'Username: {username}; Message: {message}\n')
                
    def sendMessage(self, message):
        print(message)
        url = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chatId}&text={message}'
        print(requests.get(url).json())

#Function to get the current date and give a proper fileName
def getDay():
    d = date.today()
    return d
    
#Function to get the all the articles from the page
def getListFromWeb(pageId):
    articleList = []
    url = 'https://www.todoconsolas.com/es/197-manga?order=product.name.asc&page=' + str(pageId)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', {'class': 'product-info'})
    for job_element in results:
        title = job_element.find('h1', class_='h3 product-title')
        price = job_element.find('span', class_='price')
        print(title.text,' - ' ,price.text)
        a_tags = job_element.find_all('a', href=True) 
        for tag in a_tags:
            if tag['href'] != '#':
                articleUrl = tag['href']
        dict =	[title.text, price.text, articleUrl]
        articleList.append(dict)
    print (articleList)
    return articleList

#Function to get the last page from the website
def getLastPageNumber():
    webpageNumbers = []
    URL = 'https://www.todoconsolas.com/es/197-manga?order=product.name.asc&page=1'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('ul', {'class': 'page-list clearfix text-sm-center'})
    for job_element in results:
        numbers = job_element.find_all('a', class_='js-search-link')
        for number in numbers:
            if(number.text.strip().isnumeric()):
                webpageNumbers.append(int(number.text.strip()))
    webpageNumbers.sort()
    return webpageNumbers[-1]    


if __name__ == "__main__":
    articleList = []
    for x in range(getLastPageNumber()):
        articleList.extend(getListFromWeb(x))
        
    print(articleList)
    df = pd.DataFrame(articleList, columns = ['Name', 'price', 'URL'])
    df[['type' , 'Name']] = df['Name'].str.split(n=1, expand=True)
    df['price'] = df['price'].str.replace(u'\xa0', u' ')
    df['price'] = df['price'].str.replace(' €', '')
    df['price'] = df['price'].astype(float)
    df['price'] = df['price'].div(100)
    df.to_csv(f'manga_{getDay()}.csv', sep=';')
