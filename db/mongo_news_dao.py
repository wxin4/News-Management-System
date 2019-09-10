from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao:

    # 添加新闻正文记录
    def insert(self, title, content):
        try:
            client.vega.news.insert_one({'title': title, 'content':content})
        except Exception as e:
            print(e)

    # 查找新闻正文的主键值
    def search_id(self, title):
        try:
            news = client.vega.news.find_one({'title': title})
            return str(news['_id'])
        except Exception as e:
            print(e)

    # 更改新闻标题正文内容
    def update(self, id, title, content):
        try:
            client.vega.news.update_one({'_id': ObjectId(id)},
                                        {'$set': {'title': title, 'content': content}})
        except Exception as e:
            print(e)

    # 查找新闻正文
    def search_content_by_id(self, id):
        try:
            news = client.vega.news.find_one({'_id': ObjectId(id)})
            return news['content']
        except Exception as e:
            print(e)

    # 删除新闻
    def delete_by_id(self, id):
        try:
            client.vega.news.delete_one({'_id': ObjectId(id)})
        except Exception as e:
            print(e)