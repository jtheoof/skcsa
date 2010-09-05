from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTION = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skcsa',
        'USER': 'django',
        'PASSWORD': 'dj4ng0',
        'OPTIONS': {'init_command': 'SET storage_engine=INNODB'},
    }
}
