from delivit_waitlist.settings.base import *

DEBUG = False


ALLOWED_HOSTS = ['*']


STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR).joinpath('staticfiles')
STATICFILES_DIRS = (Path(BASE_DIR).joinpath('static'),)