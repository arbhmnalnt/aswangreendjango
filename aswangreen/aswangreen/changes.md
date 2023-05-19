ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = False

ROOT_URLCONF = 'aswangreen2.urls'
WSGI_APPLICATION = 'aswangreen2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aswangreen2$data',
        'USER': 'aswangreen2',
        'PASSWORD': 'ahmed123!',
        'HOST': 'aswangreen2.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

MEDIA_ROOT = '/home/aswangreen2/aswangreen/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/aswangreen2/aswangreen/static'
STATIC_URL = '/static/'