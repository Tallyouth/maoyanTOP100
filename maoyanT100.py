
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from multiprocessing import Pool
def get_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                            ' (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    try:
        re = requests.get(url, headers=headers)
        if re.status_code == 200:
            return re.text
        return None
    except RequestException:
        return None
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('dd')
    for item in items:
        index = item.select('i')[0].text
        titles = item.select('.name')[0].text
        stars = item.select('.star')[0].text.strip('\n')
        releasetimes = item.select('.releasetime')[0].text.strip('\n')
        imgs = item.select('img[class="board-img"]')[0]['data-src']
        list = {
            'index':index,
            'title': titles,
            'star': stars,
            'releasetime': releasetimes,
            'img': imgs
        }
        print(list)
def main():
    i = int(input('你想要看第几页'))*10
    url = 'http://maoyan.com/board/4?offset={}'.format(i)
    html = get_page(url)
    parse_page(html)
if __name__ == '__main__':
    main()


