import os


class config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # 1. Fetch the database URL
    _db_url = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    
    # 2. Fix the broken Render prefix automatically if it starts with 'postgres://'
    if _db_url.startswith('postgres://'):
        _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = _db_url
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
    MAIL_DEFAULT_SENDER = os.getenv('EMAIL_USER') 