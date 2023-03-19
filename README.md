# Personal blog using Django
  - Build data models, views, and URLs
  - Implement an administration site for your blog
  - Use canonical URLs for modles and implement SEO-friendly URLs for posts
  - Build post pagination and learn how to create class-based views
  - Use forms to allow readers to share posts via email and implement a comment system using model forms
  - Add tags to posts using [django-taggit](https://github.com/jazzband/django-taggit) and recommend similar posts based on shared tags
  - Implement custom template tags to display latest posts and most commented posts
  - Implement a custom template filter to render [Markdown](https://github.com/Python-Markdown/markdown)
  - Create a sitemap and a RSS feed for your blog
  - Implement a full-text search engine using PostgreSQL

## To start the project:
1. The first thing to do is to clone the repository:
    ```
    git clone https://github.com/marik177/django_personal_blog.git
    
    cd mysite
    ```
2. Create a virtual environment to install dependencies in and activate it:
    ```
    python3 -m venv venv
   
    source venv/bin/activate
    ```   
3. Then install the dependencies:
    ```
   (env)$ pip install -r requirements.txt
    ```
    &emsp; Note the (env) in front of the prompt.

    &emsp; This indicates that this terminal session operates in a virtual environment set.


4. Once pip has finished downloading the dependencies make migrations:
    ```
    python3 manage.py migrate
    ```
5. Create superuser:
    ````
    python3 manage.py createsuperuser
    ````
   
6. Load testing data:
    ````
    python3 manage.py loaddata mysite_data.json
    `````

7. And finally run test server:
    ````
    (env)$ python3 manage.py runserver
