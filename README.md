# Simple CMS

Simple CMS is for you if:
* You do not want to make everything from scratch
* Are tired of the cms that will always force you some templates that do not allow you to customize everything as you want
* Know well HTML/CSS/JS

## Milestones:
1. Create Initial Models to represent the Templates and Articles __[x]__
2. Create scripts to parse the Template and detect the relevant areas __[x]__
3. Insert the Template and the Article associated with the template in the database __[x]__
4. Parse the Specific area tag [[ Area ]] and insert the article content in it while serving the articles __[x]__
5. Use the articles defined links instead of the article id in the url mapping __[x]__
6. Present a simple UI to manage the templates creation, update and removal __[ ]__
7. Present a simple UI to manage the articles creation, update and removal __[ ]__
8. Present a simple UI to write the articles content by area __[ ]__
9. Add simple image upload to the cms __[ ]__
10. Add uploaded images selector to insert them in the articles writing area __[ ]__ 

## Setup

1. Clone this repo
```sh
	git clone https://github.com/drmargarido/simple_csm.git
```

2. Create a new app with the django command or just edit the manager app
```sh
	python manage.py startapp <app_name>
``` 

3. Make the initial migrations to setup the database
```sh
	python manage.py makemigrations
	python manage.py migrate
```

4. Create an admin to manage and write the articles content
```sh
	python manage.py createsuperuser
```

## Managing the project

At this moment there isn't a simple dashboard to manage the articles and the templates. They can be added using the django administration dashboard but that's error prone since the areas selection and creation can be a bit strange to select because of them behing relationships. 

So some simple scripts have been added to the manage.py of the project in order to manage the templates and articles. The article content can be wrote in the admin dashboards without any trouble.

* Add new template
```sh
	python manage.py create_template <template/template_name> <template_name>
```

* Update an existing template
```sh
	python manage.py update_template <template_name>
```

* Add new article
```sh
	python manage.py create_article <template_name> <article_title> <article_link>
```

* Remove article
```sh
	python manage.py remove_article <article_id>
```

* Run the development server
```sh
	python manage.py runserver
```

## Workflow

1. Create a html template using the django template tags
2. Add the SimpleCMS tags in the final template with a name for each area [[ Area ]], [[ Other Area ]]
3. Run the script Add new template command
4. Run the add new article command for each of the wanted articles using the created template name
5. Go to the django admin dashboard at /admin/manager/
6. Go to the ArticleAreas and edit the content of each of the wanted areas
7. Access the article template by id like 127.0.0.1:8000/1/

## Deploy

* Django changes in the application before deploy [link](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/)
* To deploy the application the django server is not suitable, use something like django + uwsgi + nginx 
[link](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
