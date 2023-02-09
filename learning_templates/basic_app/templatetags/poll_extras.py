from django import template

register = template.Library()

@register.filter(name="cut_out")
def cut(value, arg):
    """Removes all values of arg from the given string"""
    value = value.lower()
    return value.replace(arg, '')

@register.filter(name="lower_all")
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()
