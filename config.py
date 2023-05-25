class SystemConfig:

  DEBUG = False

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
      'user': 'root',
      'password': 'yuta0408',
      'host': '127.0.0.1',
      'db_name': 'ratrun_advanced'
  })
  SQLALCHEMY_TRACK_MODIFICATIONS = False


# Configという名前で外部ファイルから読み込めるように
Config = SystemConfig