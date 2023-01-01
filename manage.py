#!/usr/bin/env python

from os import environ
from sys import argv

ENVPATH = 'blog/.env'
ENVTESTPATH = 'blog/.env.testing'
ENVSAMPLEPATH = 'blog/.env.example'


def main(ENVPATH):
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    try:
        from django.core.management import execute_from_command_line
        environ.setdefault('ENVPATH', ENVPATH)
        from blog import env
        print(f"Environment from: {ENVPATH}")
        print(f"Environment: {env.ENV}")
        print(f"Media Root: {env.MEDIA_ROOT}")
        print(f"Media URL: {env.MEDIA_URL}")
        print(f"Static Root: {env.STATIC_ROOT}")
        print(f"Static URL: {env.STATIC_URL}")

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(argv)


if __name__ == '__main__':
    if argv[1] == 'test':
        main(ENVPATH=ENVTESTPATH)
    else:
        main(ENVPATH=ENVPATH)
