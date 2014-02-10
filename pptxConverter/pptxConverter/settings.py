"""
Django settings for pptxConverter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Path to presentations with images
PRESENTATION_PATH = 'pptxApp/static/media/'
PRESENTATION_STATIC_PATH = '/static/media/'

#Commands for converting presentation into images. NOTE the queue of commands is important
CMD_COMMANDS = [
    'unoconv -f pdf {presentation_name}.pptx',
    'convert {presentation_name}.pdf -resize 1024x768 {image_name}',
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g+o7ex@cxbvmhvt%fndmzs-@1769+n$mn(ep6teu8!w3pcz@e!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    '{0}/pptxApp/templates'.format(BASE_DIR),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pptxApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pptxConverter.urls'

WSGI_APPLICATION = 'pptxConverter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pptx',
        'USER': 'pptx',
        'PASSWORD': 'pptx'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# STATIC_ROOT = '{0}/pptxApp/static'.format(BASE_DIR)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    '{0}/pptxApp/static'.format(BASE_DIR),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = '{0}/pptxApp/static/media'.format(BASE_DIR)

TEMPLATE_CONTEXT_PROCESSORS=(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "pptxApp.context_processor.get_presentations",
)