from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, urls):
    print context['request'].path, [ reverse(url) for url in urls.split() ]
    if context['request'].path in ( reverse(url) for url in urls.split() ):
        return 'class="active"'
    return ""