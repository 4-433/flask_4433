HOST = '0.0.0.0'
PORT = 5000
DEBUG = False
PAUSED = True  # PAUSED:True(关闭定时任务), False(打开定时任务)
TOKEN_EXPIRATION = 60 * 60 * 2
SQLALCHEMY_ECHO = False  # 是否打印底层SQL
SCHEDULER_TIMEZONE = 'Asia/Shanghai'
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 全局上传文件大小
