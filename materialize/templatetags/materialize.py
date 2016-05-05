__author__ = 'W'
from django.template import loader

from django import template
register = template.Library()


@register.simple_tag()
def materialize_form(*args, **kwargs):
    return render_form(*args, **kwargs)

def render_form(form, form_title='', data_success='', data_error=''):
    t = loader.get_template('forms/simple_form.html')
    c = {
        'form': form,
        'data_success':data_success,
        'data_error':data_error,
        'form_title':form_title,
     }
    html = t.render(c)
    return html
