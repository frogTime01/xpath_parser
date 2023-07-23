import requests
from lxml import html


def parser_mail_news():
    url = 'https://news.mail.ru/'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    response = requests.get(url=url, headers=headers)
    news = []
    if response.ok:
        dom = html.fromstring(response.text)
        items = dom.xpath("//html//div[contains(@class, 'newsitem')]")
        for item in items:
            if item.xpath(".//a/@href"):
                headline = {}
                headline["source"] = url
                headline["link"] = item.xpath(".//a/@href")[0]
                headline["name"] = item.xpath(
                    ".//span[contains(@class, 'newsitem__title')]//text()")[0]
                resp = requests.get(url=headline["link"], headers=headers)
                if resp.ok:
                    dom_link = html.fromstring(resp.text)
                    headline["date"] = dom_link.xpath(
                        "//html//div[contains(@class, 'breadcrumb')]//@datetime")[0]
                news.append(headline)
    return news
