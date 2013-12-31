try:
    from jinja2 import Template

    def jinja2_filter(text, context):
        template = Template(text)
        return template.render(context)
except ImportError:
    pass
