from django import template

register = template.Library()


@register.filter(name='space_to_dash')
def space_to_dash(value):
    return value.replace(' ', '-')


@register.filter(name='dash_to_space')
def dash_to_space(value):
    return value.replace('-', ' ')
