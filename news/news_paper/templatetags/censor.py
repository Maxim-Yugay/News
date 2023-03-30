from django import template


register = template.Library()

sens = [
        'article',
    ]

@register.filter()
def censor(text):
    t1 = text.split()
    for t in t1:
        if t == sens:
            t = '***'
            return t1



