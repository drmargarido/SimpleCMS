# Simple CMS

Simple CMS is for you if:
* You do not want to make everything from scratch
* Are tired of the cms that will always force you some templates that do not allow you to customize everything as you want
* Want something more secure than the big CMS
* Know well HTML/CSS/JS

## Milestones:
1. Create Initial Models to represent the Templates and Articles __[x]__
2. Create scripts to parse the Template and detect the relevant areas __[x]__
3. Insert the Template and the Article associated with the template in the database __[x]__
4. Parse the Specific area tag [[ Area ]] and insert the article content in it while serving the articles __[x]__
5. Present a simple UI to manage the templates creation, update and removal []
6. Present a simple UI to manage the articles creation, update and removal []
7. Present a simple UI to write the articles content by area []

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