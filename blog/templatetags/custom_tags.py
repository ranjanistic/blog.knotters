from random import randint
from re import sub as re_sub
from urllib.parse import unquote

from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter(name='or')
def useOR(value, Or):
    return value or Or


@register.filter(name='safechars')
def safechars(value):
    return str(value).replace('\\n', '\n').replace('\"', '').replace('\\', '\"').replace('&lt;', '[').replace('&gt;', ']')

@register.filter(name='noprotocol')
def noprotocol(link):
    if str(link).startswith(('http', 'https')):
        link = link.replace('https://', '')
        link = link.replace('http://', '')
    return link


@register.filter(name='getquery')
def getquery(url, querydata: str):
    querydata = str(querydata).replace(
        ',', '&').replace('\'', '').replace('\"', '')
    return f"{url}?{querydata}"


@register.filter(name='urldecode')
def urldecode(value):
    return unquote(value)


@register.filter(name='onezero')
def onezero(one, boolpair=None):
    if boolpair:
        yes, no = boolpair.split("|")
    else:
        yes, no = 1, 0
    return yes if one else no


@register.filter(name='publicprivateicon')
def publicprivateicon(public):
    return "lock_open" if public else "lock"


@register.simple_tag
def random_int(a=1, b=100):
    return randint(a, b)

@register.filter(name='inlist')
def inlist(thelist=[], value=None):
    return value in thelist

@register.filter(name='display_number')
def display_number(value=0, num_decimals=2):
    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('.0') + 'K'
    else:
        return formatted_number.format(int_value/1000000.0).rstrip('.0') + 'M'
