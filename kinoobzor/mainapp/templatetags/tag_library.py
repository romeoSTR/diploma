from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)


@register.filter()
def add_ss_to_item(value):
    if value == 'film':
        return f"{value}ss"
    else:
        return f"{value}s"
