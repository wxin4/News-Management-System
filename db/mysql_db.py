import mysql.connector.pooling
__config = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '@Lbq54824674',
    'database' : 'vega',
    'auth_plugin' :'caching_sha2_password'
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name = 'mypool',
        pool_size=10,
        **__config
    )
except ImportError as e:
    print(e)
