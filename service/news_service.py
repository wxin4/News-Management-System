from db.news_dao import NewsDao
from db.redis_news_dao import RedisNewsDao
from db.mongo_news_dao import MongoNewsDao

class NewsService:
    __news_dao = NewsDao()
    __redis_news_dao = RedisNewsDao()
    __mongo_news_dao = MongoNewsDao()

    # 查询待审批新闻列表
    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询新闻列表
    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result

    # 查询新闻总页数
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()
        return count_page

    # 删除新闻
    def delete_by_id(self, id):
        content_id = self.__news_dao.search_content_id(id)
        self.__news_dao.delete_by_id(id)
        self.__mongo_news_dao.delete_by_id(content_id)

    # 添加新闻
    def insert(self, title, editor_id, type_id, content, is_top):
        self.__mongo_news_dao.insert(title, content)
        content_id = self.__mongo_news_dao.search_id(title)
        self.__news_dao.insert(title, editor_id, type_id, content_id, is_top)

    # 查询用户缓存的记录
    def search_cache(self, id):
        result = self.__news_dao.search_cache(id)
        return result

    # 向Redis保存缓存的新闻
    def cache_news(self, id, title, username, type, content, is_top, create_time):
        self.__redis_news_dao.insert(id, title, username, type, content, is_top, create_time)

    # 删除缓存新闻
    def delete_cache(self, id):
        self.__redis_news_dao.delete_cache(id)

    # 根据id查找新闻
    def search_by_id(self, id):
        result = self.__news_dao.search_by_id(id)
        return result

    # 更改新闻
    def update(self, id, title, type_id, content, is_top):
        content_id = self.__news_dao.search_content_id(id)
        self.__mongo_news_dao.update(content_id, title, content)
        self.__news_dao.update(id, title, type_id, content_id, is_top)
        self.delete_cache(id)

    # 查找新闻正文
    def search_content_by_id(self, id):
        content = self.__mongo_news_dao.search_content_by_id(id)
        return content