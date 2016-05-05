from django.template import loader
from django import template
register = template.Library()

@register.filter()
def get_value(value):
    return ('{{i.id}}')

@register.filter(name='file_input')
def field_type(field):
    name = get_field_type(field)
    if name == 'ClearableFileInput' or name == 'FileInput':
        return True
    return False

@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__

def get_field_type(field):
    return field.field.widget.__class__.__name__

@register.filter(name='addcss')
def addcss(field, css):
    type_input = get_field_type(field)
    if type_input == 'Textarea':
        css = 'materialize-textarea'
    if type_input == 'CheckboxSelectMultiple':
        return render_checkbox(field)
    if type_input == 'RadioSelect':
        return render_radio(field)
    if type_input == 'ClearableFileInput':
        return render_file(field)
    if type_input == 'DateInput':
        return field.as_widget(attrs={"type":'date',"class":'datepicker'})
    return field.as_widget(attrs={"class":css})


def render_checkbox(field):
    t = loader.get_template('forms/render_checkbox.html')
    c = {
        'field': field,
     }
    html = t.render(c)
    return html

def render_radio(field):
    t = loader.get_template('forms/render_radio.html')
    c = {
        'field': field,
     }
    html = t.render(c)
    return html

def render_file(field):
    t = loader.get_template('forms/render_file.html')
    c = {
        'field': field,
     }
    html = t.render(c)
    return html