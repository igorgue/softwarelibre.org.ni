# Django settings for softwarelibre project.
import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

ADMINS = (
    ('Adolfo Fitoria', 'adolfo@fitoria.net'),
    ('Igor Guerrero', 'igfgt1@gmail.com'),
)

# adding the apps dir to the path
APPS_DIR = PROJECT_DIR + '/apps'
APPS_PATH_COUNT = sys.path.count(APPS_DIR)

if APPS_PATH_COUNT == 0:
    sys.path.insert(1, PROJECT_DIR + '/apps')
else:
    for i in range(0, APPS_PATH_COUNT):
        sys.path.remove(APPS_DIR)
    sys.path.insert(1, PROJECT_DIR + '/apps')


MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = PROJECT_DIR + '/development.sqlite'
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Managua'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ni'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_DIR + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i)b1_64q5c9bdzuq+xjj%(gtsja-wiqq@du-v4+br2j_mod44!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'softwarelibre.urls'

TEMPLATE_DIRS = (
    PROJECT_DIR + "/templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'softwarelibre.apps.registration',
    'softwarelibre.apps.planet',
    'softwarelibre.apps.profiles',
    'softwarelibre.apps.tagging',
    'softwarelibre.apps.answers',
)

#Registration Settings
ACCOUNT_ACTIVATION_DAYS = 3
AUTH_PROFILE_MODULE = 'profiles.UserProfile'
LOGIN_REDIRECT_URL = '/planet/'

EMAIL_SETTINGS = {"from": "noresponder@softwarelibre.org.ni", "subject": "notificacion del sitio", "signature": "Software Libre Nicaragua"}

