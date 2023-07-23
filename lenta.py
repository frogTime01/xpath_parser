import requests
from lxml import html


def parser_lenta_news():
    """only the main news"""
    url = 'https://lenta.ru'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url=url, headers=headers)
    news = []
    if response.ok:
        dom = html.fromstring(response.text)
        items = dom.xpath("//html//div[contains(@class, 'last24')]//a")
        for item in items:
            headline = {}
            headline["source"] = url
            headline["link"] = url + item.xpath("./@href")[0]
            headline["name"] = item.xpath(".//h3//text()")[0]
            resp = requests.get(url=headline["link"], headers=headers)
            if resp.ok:
                dom_link = html.fromstring(resp.text)
                headline["date"] = dom_link.xpath(
                    "//html//a[contains(@class, 'time')]//text()")[0]
            news.append(headline)
    return news
