import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    LANGUAGES = ['en', 'ru', 'es']
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gjk28fd058g03'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['redduck5601@example.com']

    POSTS_PER_PAGE = 24
