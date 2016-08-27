import os


# =============================================================================
# Which WEB_ENV?
# =============================================================================
# Valid options - local, dev, qa, prod
from manage import PROJECT_ROOT

WEB_ENV = 'local'

# Branch and version number
# BRANCH = 'master'
# VERSION = 'v0.0.0'
DEBUG = True
SITE_ID = "1"
SECRET_KEY = "68h(iy4+r@y2rh-t+*#s_-p1z%kfgdfe%$$#%nqf6lzw(9bh^&"
# =============================================================================
# PATHS
# =============================================================================
# Full filesystem path to the project.
# based on common.py is in <PROJECT_ROOT>/settings

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT

# Package/module name to import the root urlpatterns from for the project.
# ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
ROOT_URLCONF = "settings.urls"

# Put strings here, like "/home/html/django_templates"
# or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'rest_framework',
    'django_extensions',
    'product'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# create database app_db;
# grant all on app_db.* to 'app_admin' identified by 'App_admin123';
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}
# Connect to MongoDB

# connect('leave_test_db', host='localhost', port=27017,
#         alias='default')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# This fucking thing keeps on irritating but now it wont
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static"),)
STATIC_URL = '/static/'

COMPRESS_ROOT = "static/CACHE"
# C0MPRESS_ROOT = PROJECT_ROOT + 'static/CACHE/'
MEDIA_ROOT = 'static/media'

# STATIC_ROOT = PROJECT_ROOT + "static/"

MEDIA_URL = STATIC_URL + "media/"
# MEDIA_ROOT = PROJECT_ROOT + 'static/media/'

UPLOAD_ROOT = MEDIA_ROOT + "media/uploads/"
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads/")

# This fucking thing keeps on irritating but now it wont

COMPRESS_ENABLED = True
