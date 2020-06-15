import requests
from bs4 import BeautifulSoup as bs

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
        soup = bs(html,'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            result_news.append({
                'title':title,
                'url':url,
                'published':published
            })
        return result_news
    return False
#if __name__ == "__main__":
#    html = get_html("https://www.python.org/blogs/")
#    if html:
#        get_python_news(html)
#
#        with open("python.org.html","w",encoding="utf8") as f:
#            f.write(html)
