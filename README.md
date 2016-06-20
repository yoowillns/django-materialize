=====
Materialize for Django
=====

Materialize is a simple implementation of ``materializecss`` for Django.

More information on ``materializecss``

http://materializecss.com/

Requirements
------------

- Python >= 2.7
- Django >= 1.8


## Table of Contents
- [Part 1: Quick start ](#quick-start)
  - [1.1: Install](#install)
  - [1.2: Project Structure](#project-structure)
  - [1.3: Template Main Layout](#template-main-layout)
  - [1.4: Template Content](#template-content)
- [Part 2: Examples](#examples)
  - [2.1: Model Example](#model-example)
  - [2.2: Model Form Example](#model-form-example)
  - [2.3: Template Form Example](#template-form-example)
  - [2.4: Result Form](#result-form)
- [Part 3: Extra](#extra)
  - [3.1: Customize Label Erros](#customize-label-erros)

---

## Quick start 

Download ZIP or clone this repository (https://github.com/yoowillns/django-materialize) 

### Install

1. Install:

   ``setup.py install``

2. Add "materialize" to your INSTALLED_APPS settings :
    ```python
    INSTALLED_APPS = [
        ...
        'materialize',
    ]
    ```
3. In your templates, load the ``materialize`` library and use the ``{% load materialize %}`` 

### Project Structure
  
  Create templates folder in project: `/templates/layout/MainLayout.html`

### Template Main Layout

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Materialize Demo</title>
    <!-- Include static files in project -->
    {% include 'lib/materialize_static.html' %}
</head>
<body>
    <div class="container">
        {% block content %}
        <!-- Content project -->
        {% endblock %}
    </div>
</body>
</html>
```

### Template Content

```python

{% extends 'layouts/MainLayout.html' %}

{% load materialize %}

{% block content %}
    <div class="row">
        <div class="col s6">
            <form class="col s12" action="" method="post">
                {% csrf_token %}

                {% materialize_form form %}

                <button class="btn waves-effect waves-light" type="submit" name="action">Register
                </button>
            </form>
        </div>
    </div>
{% endblock %}
```

## Examples

### Model Example

```python
from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=10, verbose_name='Nombre', null=False)
  category = models.ManyToManyField(Category, verbose_name='Categoria')
  count = models.IntegerField(verbose_name='Cantidad')
  date_buy = models.DateField(verbose_name='Fecha de Compra')
  image = models.FileField(upload_to='uploads', verbose_name='Imagen')
  description = models.TextField(verbose_name='Descripcion')
  state = models.BooleanField(verbose_name='Estado', default=False)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.name

  class Meta:
      verbose_name = 'Producto'
      verbose_name_plural = 'Productos'
```       

### Model Form Example

```python
from django import forms
from django.forms import ModelForm
from models import *

class ProductForm(forms.ModelForm):
  class Meta:
      model = Product
      fields = '__all__'
```

### Template Form Example

```python

{% extends 'layouts/MainLayout.html' %}

{% load materialize %}

{% block content %}
    <div class="row">
        <div class="col s6">
            <form class="col s12" action="" method="post" enctype="multipart/form-data">
                {% csrf_token %}

                {% materialize_form form form_title='Producto' data_success='Correcto' %}
                
                <button class="btn waves-effect waves-light" type="submit" name="action">Register
                </button>
            </form>
        </div>
    </div>
{% endblock %}
```

### Result Form

![alt text](https://github.com/yoowillns/screenshots/blob/master/demos/materialize-form-1.png "Demo Form")

## Extra
### Customize Label Erros
  Use class `.label-error` in css style in project



