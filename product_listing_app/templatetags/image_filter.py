from atexit import register
from django import template

register = template.Library()

@register.filter
def encode_image(value):
    if value is not None:
        import base64
        return base64.b64encode(value).decode("utf-8")