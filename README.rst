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

Quick start download ZIP or clone this repository 
-----------
1. Install:

   ``setup.py install``

2. Add "materialize" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'materialize',
    ]

3. Add "materializecss" in base template in django::
	
Example template base.html
----------------
	.. code:: Django

	<!-- Compiled and minified CSS -->
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.6/css/materialize.min.css">

	<!--Import jQuery before materialize.js-->
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>

	<!-- Compiled and minified JavaScript -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.6/js/materialize.min.js"></script>

Or download files " materializecss " http://materializecss.com/bin/materialize-v0.97.6.zip and copy in the `` static`` of your project and load your templates

4. In your templates, load the ``materialize`` library and use the ``{% load materialize %}`` 

Example template
----------------

   .. code:: Django

    {% load materialize %}

	{% block content %}

	    <div class="row">
	        <div class="col s12">
	            <form class="col s12" action="" method="post">
	                {% csrf_token %}

	                {% materialize_form form %}

	                <button class="btn waves-effect waves-light" type="submit" name="action">Register
	                </button>
	            </form>
	        </div>
	    </div>

	{% endblock %}


