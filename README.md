# Short-URL

=====
urlshorterapp
=====

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "urlshorterapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'urlshorterapp',
    ]
2. Add   this line to settings file  :     MAXIMUM_URL_CHARS = 10 

	 This Responsible for specifying the length of the generated text.

	 If you do not specify it, it takes a default value of 7   

3. Include the polls URLconf in your project urls.py like this::

    path('',include('urlshorterapp.urls')),

3. Run ``python manage.py makemigrations `` .

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   
5. Visit http://127.0.0.1:8000/short_url/  .
