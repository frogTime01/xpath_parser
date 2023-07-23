from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from mail import parser_mail_news
from lenta import parser_lenta_news


if __name__ == '__main__':
    client = MongoClient("127.0.0.1", 27017)
    db_news = client["db_vacancy"]
    collection_news = db_news.collection_news

    mail_news = parser_mail_news()
    lenta_news = parser_lenta_news()
    collection_news.insert_many(mail_news)
    collection_news.insert_many(lenta_news)

    print(collection_news.count_documents({}))
    for news in collection_news.find({}):
        pprint(news)

    db_news.drop_collection('collection_news')
    client.close()
