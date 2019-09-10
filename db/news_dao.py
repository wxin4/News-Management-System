from db.mysql_db import pool

class NewsDao:
    # 查询待审批新闻列表
    def search_unreview_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "JOIN t_user u ON n.editor_id = u.id " \
                  "WHERE n.state = %s " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s, %s"
            cursor.execute(sql, ('待审批', (page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*) / 10) FROM t_news WHERE state = %s"
            cursor.execute(sql, ['待审批'])
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 审批新闻
    def update_unreview_news(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET state = %s WHERE id = %s"
            cursor.execute(sql, ('已审批', id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻列表
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.id, n.title, t.type, u.username " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "JOIN t_user u ON n.editor_id = u.id " \
                  "ORDER BY n.create_time DESC " \
                  "LIMIT %s, %s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询新闻总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT CEIL(COUNT(*) / 10) FROM t_news"
            cursor.execute(sql)
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 删除新闻
    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_news WHERE id = %s"
            cursor.execute(sql, (id,))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 添加新闻
    def insert(self, title, editor_id, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_news(title, editor_id, type_id, content_id, is_top, state) " \
                  "VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (title, editor_id, type_id, content_id, is_top,"待审批"))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查询用户缓存的记录
    def search_cache(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title, u.username, t.type, n.content_id, n.is_top, n.create_time " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "JOIN t_user u ON n.editor_id = u.id " \
                  "WHERE n.id = %s"
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 根据id查找新闻
    def search_by_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT n.title, t.type, n.is_top " \
                  "FROM t_news n " \
                  "JOIN t_type t ON n.type_id = t.id " \
                  "WHERE n.id = %s"
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 更改新闻
    def update(self, id, title, type_id, content_id, is_top):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_news SET title = %s, type_id = %s, " \
                  "content_id = %s, is_top = %s, state = %s, " \
                  "update_time = NOW() " \
                  "WHERE id = %s"
            cursor.execute(sql, (title, type_id, content_id, is_top,"待审批", id))
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()

    # 查找内容id
    def search_content_id(self, id):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT content_id FROM t_news " \
                  "WHERE id = %s"
            cursor.execute(sql, [id])
            content_id = cursor.fetchone()[0]
            return content_id
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()