import os  # isort:skip

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))

from . import env
from pathlib import Path

BASE_DIR = env.BASE_DIR
SECRET_KEY = env.PROJECTKEY

DEBUG = not env.ISPRODUCTION

ALLOWED_HOSTS = env.HOSTS

ROOT_URLCONF = 'blog.urls'

CDN_URL = env.CDN_URL

WSGI_APPLICATION = 'blog.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATA_UPLOAD_MAX_MEMORY_SIZE = 10*1024*1024

STATIC_URL = env.STATIC_URL
MEDIA_ROOT = env.MEDIA_ROOT
MEDIA_URL = env.MEDIA_URL


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

if not env.STATIC_ROOT in STATICFILES_DIRS:
    STATIC_ROOT = env.STATIC_ROOT
elif DEBUG:
    STATIC_ROOT = env.STATIC_ROOT

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                "blog.context_processors.Global",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                "django.template.context_processors.i18n",
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'blog'
]

LANGUAGES = (
    ('af', 'Afrikaans'),
    ('ar', 'عربي'),
    ('ast', 'Asturian'),
    ('az', 'Azərbaycanca'),
    ('bg', 'български'),
    ('be', 'Беларуская'),
    ('bn', 'বাংলা'),
    ('br', 'Breton'),
    ('bs', 'Bosanski'),
    ('ca', 'Català'),
    ('cs', 'čeština'),
    ('cy', 'Cymraeg'),
    ('da', 'dansk'),
    ('de', 'Deutsch'),
    ('dsb', 'Lower Sorbian'),
    ('el', 'Ελληνικά'),
    ('en', 'English'),
    ('en-au', 'Australian English'),
    ('en-gb', 'British English'),
    ('eo', 'Esperanto'),
    ('es', 'Español'),
    ('es-ar', 'Argentinian Spanish'),
    ('es-co', 'Colombian Spanish'),
    ('es-mx', 'Mexican Spanish'),
    ('es-ni', 'Nicaraguan Spanish'),
    ('es-ve', 'Venezuelan Spanish'),
    ('et', 'Eestlane'),
    ('eu', 'Euskara'),
    ('fa', 'فارسی'),
    ('fi', 'Suomalainen'),
    ('fr', 'français'),
    ('fy', 'Frysk'),
    ('ga', 'Gaeilge'),
    ('gd', 'Gàidhlig na h-Alba'),
    ('gl', 'Galego'),
    ('he', 'Hebrew'),
    ('hi', 'हिंदी'),
    ('hr', 'Hrvatski'),
    ('hsb', 'Upper Sorbian'),
    ('hu', 'Magyar'),
    ('hy', 'հայերեն'),
    ('ia', 'Interlingua'),
    ('id', 'bahasa Indonesia'),
    ('io', 'Ido'),
    ('is', 'Íslensku'),
    ('it', 'italiano'),
    ('ja', '日本'),
    ('ka', 'ქართული'),
    ('kab', 'Kabyle'),
    ('kk', 'Қазақша'),
    ('km', 'ខ្មែរ'),
    ('kn', 'ಕನ್ನಡ'),
    ('ko', '한국인'),
    ('lb', 'Lëtzebuergesch'),
    ('lt', 'Lietuvių'),
    ('lv', 'Latvietis'),
    ('mk', 'Македонски'),
    ('ml', 'മലയാളം'),
    ('mn', 'Монгол'),
    ('mr', 'मराठी'),
    ('my', 'ဗမာ'),
    ('nb', 'Norwegian Bokmål'),
    ('ne', 'नेपाली'),
    ('nl', 'Nederlands'),
    ('nn', 'Norwegian Nynorsk'),
    ('os', 'Ossetic'),
    ('pa', 'ਪੰਜਾਬੀ'),
    ('pl', 'Polskie'),
    ('pt', 'português'),
    ('pt-br', 'Brazilian Portuguese'),
    ('ro', 'Română'),
    ('ru', 'русский'),
    ('sk', 'Slovenský'),
    ('sl', 'Slovenščina'),
    ('sq', 'Shqiptare'),
    ('sr', 'Српски'),
    ('sr-latn', 'Serbian Latin'),
    ('sv', 'svenska'),
    ('sw', 'Kiswahili'),
    ('ta', 'தமிழ்'),
    ('te', 'తెలుగు'),
    ('th', 'ไทย'),
    ('tr', 'Türk'),
    ('tt', 'Tatar'),
    ('udm', 'Udmurt'),
    ('uk', 'Українська'),
    ('ur', 'اردو'),
    ('uz', "O'zbek"),
    ('vi', 'Tiếng Việt'),
    ('zh-hans', 'Simplified Chinese'),
    ('zh-hant', 'Traditional Chinese'),

)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
#    ('fullwidth.html', 'Fullwidth'),
 #   ('sidebar_left.html', 'Sidebar Left'),
  #  ('sidebar_right.html', 'Sidebar Right'),
    ('blog.html', 'Blog'),
)
CMS_COLOR_SCHEME = "auto"
CMS_COLOR_SCHEME_TOGGLE = True
CMS_TOOLBAR_ANONYMOUS_ON = False
X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_HEALTH_CHECKS': 'False',
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': env.DB_NAME,
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


if not DEBUG:
    os.environ["HTTPS"] = "on"
    os.environ["wsgi.url_scheme"] = "https"
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_TRUSTED_ORIGINS = env.HOSTS
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_REFERRER_POLICY = "same-origin"
    SECURE_HSTS_PRELOAD = True
    DEFAULT_HTTP_PROTOCOL = "https"
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"


if not DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": "INFO", "handlers": ["file"]},
        "handlers": {
            "file": {
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": env.env.get_value("LOGFILE", default='_logs_/server.log'),
                "formatter": "app",
                'maxBytes': 1024*1024*5,
                'backupCount': 5
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "INFO",
                "propagate": True
            },
        },
        "formatters": {
            "app": {
                "format": (
                    u"%(asctime)s [%(levelname)-8s] "
                    "(%(module)s.%(funcName)s) %(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
    }
