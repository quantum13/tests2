from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
def dict_key(dict, key):
    return dict.get(key, '')
