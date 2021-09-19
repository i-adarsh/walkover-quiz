from .base import *

ALLOWED_HOSTS = ['3.80.106.174']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'walkover_quiz',
        'USER': 'quiz',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'POST': '3306',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}