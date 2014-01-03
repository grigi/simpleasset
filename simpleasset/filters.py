"""
Python filer functions
"""

try:
    from jinja2 import Template

    def jinja2_filter(text, context):
        "Filter blob through jinja2"
        template = Template(text)
        return template.render(context)
except ImportError:
    pass
