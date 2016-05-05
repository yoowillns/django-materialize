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



@register.simple_tag()
def materialize_table(*args, **kwargs):
    return render_table(*args, **kwargs)


def render_table(model, instance, table_title=''):
    objects = model
    fields = []

    for field in instance._meta.fields:
        fields.append({'id': field.name, 'name': field.verbose_name.title()})

    for object in model:
        object.fields = dict((field.name, field.value_to_string(object))
                                            for field in object._meta.fields)
    t = loader.get_template('tables/simple_table.html')
    c = {
        'model': model,
        'objects':objects,
        'fields':fields,
     }
    html = t.render(c)
    return html