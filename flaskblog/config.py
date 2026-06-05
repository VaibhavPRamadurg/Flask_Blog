import os


class config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.getenv('DATABASE_URL', 'sqlite:///site.db')
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
    MAIL_DEFAULT_SENDER = os.getenv('EMAIL_USER') 