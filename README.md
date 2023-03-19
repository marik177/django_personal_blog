The first thing to do is to clone the repository:
$ git clone https://github.com/marik177/django_personal_blog.git
$ cd mysite

Create a virtual environment to install dependencies in and activate it:
$ python3 -m venv venv
$ source venv/bin/activate

Then install the dependencies:
(env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. 
This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies make migrations:
$ python manage.py migrate

Create superuser:
$ python manage.py createsuperuser

Load testing data:
$ python manage.py loaddata mysite_data.json

And finally run test server:
(env)$ python manage.py runserver
