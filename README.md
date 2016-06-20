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
- [Part 3: Extra](#extra)
    - [3.1.1: Customize label erros](#customize-label-errors)

---

## Quick start 

Download ZIP or clone this repository (https://github.com/yoowillns/django-materialize) 

### Install

Our stack usually consists of the following tools:

1. Install:

   ``setup.py install``

2. Add "materialize" to your INSTALLED_APPS setting like this::
	
    INSTALLED_APPS = [
        ...
        'materialize',
    ]

3. In your templates, load the ``materialize`` library and use the ``{% load materialize %}`` 

### Project Structure

**Note:**

> - Create ``/templates/layout/MainLayout.html`` in project

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

   .. code:: Django

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

## Examples

### Model Example

   .. code:: Django

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

### Model Form Example

   .. code:: Django
     from django import forms
     from django.forms import ModelForm
     from models import *
     
     class ProductForm(forms.ModelForm):
      favorite_colors = forms.ChoiceField(required=True,
          widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES, help_text='Select')
      class Meta:
          model = Product
          fields = '__all__'


### Template Form Example

   .. code:: Django

    {% load materialize %}

    {% block content %}
        <div class="row">
            <div class="col s6">
                <form class="col s12" action="" method="post" enctype="multipart/form-data">
                    {% csrf_token %}

                    {% materialize_form form %}
                    
                    <button class="btn waves-effect waves-light" type="submit" name="action">Register
                    </button>
                </form>
            </div>
        </div>
    {% endblock %}

## Extra
### Customize label erros
Use class `.label-error` in css style in project



