from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
from webapp.model import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Network Error")
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = bs(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)


def save_news(title, url, published):   #передаём данные в базу
    news_exists = News.query.filter(News.url == url).count() #посчитает кол. новостей по url
    print(news_exists)
    if not news_exists:
        news_news = News(title = title, url = url, published = published)
        db.session.add(news_news)           #кладем в сессию базы
        db.session.commit()                 #сохранение новости в базу