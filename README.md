# Short-URL


urlshorterapp
=====

Short-URL is a Django app to make short url 


Quick start
-----------

1. Add "urlshorterapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
    
        ...
        'urlshorterapp',
	
    ]
    
2. Add this line to settings file::     MAXIMUM_URL_CHARS = 10 

	 This Responsible for specifying the length of the generated text.

	 If you do not specify it, it takes a default value of 7   

3. Include the urlshorterapp URLconf in your project urls.py like this::

    path('',include('urlshorterapp.urls')),

3. Run ``python manage.py makemigrations `` .

4. Run ``python manage.py migrate`` to create the polls models.

5. Visit http://127.0.0.1:8000/short_url/  .
