from django import template

register = template.Library()

@register.filter
def floatdivide(value, divisor):
    try:
        return float(value) / float(divisor)
    except (ValueError, ZeroDivisionError, TypeError):
        return 0
