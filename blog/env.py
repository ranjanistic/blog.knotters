"""
Loads environment variables from file path specified in ENVPATH environment variable beforehand (generally main/.env).
"""
from os import path as os_path
from pathlib import Path

from environ import Env

class Environment():
    DEVELOPMENT = 'development'
    TESTING = 'testing'
    PRODUCTION = 'production'


env = Env()

BASE_DIR = Path(__file__).resolve().parent.parent

Env.read_env(env_file=os_path.join(BASE_DIR, env('ENVPATH')))

PROJECTKEY = env('PROJECTKEY')
PUBNAME = env('PUBNAME').strip()
ENV = env('ENV').strip()
HOSTS = env('HOSTS').split(',')
ADMINPATH = env('ADMINPATH').strip()
SITE = env('SITE').strip()
STATIC_URL = env('STATIC_URL').strip()
MEDIA_URL = env('MEDIA_URL').strip()
STATIC_ROOT = env('STATIC_ROOT').strip()
MEDIA_ROOT = env('MEDIA_ROOT', default=os_path.join(BASE_DIR, 'media')).strip()

CDN_URL = env('CDN_URL', default='https://cdn.knotters.org').strip()
DB_NAME = env('DB_NAME', default='project.db').strip()
INTERNAL_SHARED_SECRET = env(
    'INTERNAL_SHARED_SECRET', default='secret').strip()

PROJECTKEY = None if PROJECTKEY == 'none' else PROJECTKEY
PUBNAME = None if PUBNAME == 'none' else PUBNAME
ENV = None if ENV == 'none' else ENV
HOSTS = None if HOSTS == 'none' else HOSTS
ADMINPATH = None if ADMINPATH == 'none' else ADMINPATH
SITE = None if SITE == 'none' else SITE
MEDIA_URL = None if MEDIA_URL == 'none' else MEDIA_URL
STATIC_URL = None if STATIC_URL == 'none' else STATIC_URL
STATIC_ROOT = None if STATIC_ROOT == 'none' else STATIC_ROOT

ISPRODUCTION = ENV == Environment.PRODUCTION

ISDEVELOPMENT = ENV == Environment.DEVELOPMENT

ISTESTING = ENV == Environment.TESTING
