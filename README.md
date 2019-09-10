# News Management System (Python-SQL)
A news managing project Of connecting SQL using Python. The whole system can do the following: adding users in editor type or admin type, adding or deleting news and users, and caching news into the database system.

#What are the main languages
-Python
-MySQL
-Redis
-MongoDB
# What does each language do
-Python is the brain of the project which connects all three database languages to do different parts of it.
-MySQL is used to manage user information, including user login, user profile management, how many pages of users are there, etc.
-Redis is used to manage cached data, including adding news and deleting news. All the news have a time limit which is 24hours. Also, when a cached news is re-edited by an editor, the previous cached news should be deleted by the admin.
-MongoDB is used to manage the main body of a piece of news. Other ralational databases or non-relational databases do not have this function or not strong enough to hold long text. Therefore, we use mongoDB to edit main body of news which is so long to manage using other database languages.
