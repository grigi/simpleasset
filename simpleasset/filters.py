"""
Python filer functions
"""

# Jinja2 Template filter
try:
    from jinja2 import Template as jinja2_Template

    def jinja2_filter(text, context):
        "Filter blob through jinja2"
        return jinja2_Template(text).render(context)
except ImportError:
    pass

# Django Template filter
try:
    from django import template as django_template

    def django_template_filter(text, context):
        "Filter blob through Django templating engine"
        return django_template.Template(text).render(django_template.Context(context))
except ImportError:
    pass

# Generic Template filter
#  First try to use Jinja2, else Django
#  Will be undefined if neither exists
if 'jinja2_filter' in dir():
    generic_template_filter = jinja2_filter
elif 'django_template_filter' in dir():
    generic_template_filter = django_template_filter