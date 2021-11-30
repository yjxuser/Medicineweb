
class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:lhllhl828..@bj-cynosdbmysql-grp-eloic4ac.sql.tencentcdb.com:21320/BioPlatform"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

