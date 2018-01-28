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
6. Add initial page where all the registered articles are shown, with a link to their page __[x]__
7. Present a simple UI to manage the templates creation, listing and disabling __[x]__
8. Present a simple UI to manage the articles creation, update and removal __[x]__
9. Present a simple UI to write the articles content by area __[x]__
10. Allow only to logged users to manage the templates and articles __[x]__
11. Present screenshots of the platform so the features will be more easily understood __[x]__ 

## Setup

1. Clone this repo
```sh
	git clone https://github.com/drmargarido/SimpleCMS.git
```

2. Make the initial migrations to setup the database
```sh
	python manage.py makemigrations
	python manage.py migrate
```

3. Create an admin to manage and write the articles content
```sh
	python manage.py createsuperuser
```

4. Running the development server
```sh
	python manage.py runserver
```

5. Edit the manager app to fit your needs
	* New templates should be added in the manager/templates/manager folder, or the folder should be changed
	* The initial index.html page is extremely simple, if you want the visitors to have a better page, rewrite the index.html page, or edit the urls mapping.

6. If you have interest in more features create a issue with them, contact me drmargarido@gmail.com or implement it and send a pull request :) .

## Features

### Regular User 

* See the existing articles
![Articles List](/readme_images/visitor_article_list.png)

* Go to each article page
![Article Page](/readme_images/article_page.png)

* Login using the django admin dashboard
![Article Page](/readme_images/login.png)

### Logged User

* See the existing active templates and disable them if wanted
![Templates List](/readme_images/list_templates.png)

* Add new template in the dashboards area
![Add Template](/readme_images/add_new_template.png)
![Template Example](/readme_images/example_template.png)

* See the existing articles, acess count and remove article if wanted
![Articles List](/readme_images/list_articles.png)

* Add new article
![Add Article](/readme_images/add_new_article.png)

* Edit article areas content
![Edit Article Page](/readme_images/edit_article_page.png)
![Edit Content](/readme_images/edit_article_content.png)

## Workflow

1. Create a html template using the django template tags
2. Add the SimpleCMS tags in the final template with a name for each area [[ Area ]], [[ Other Area ]]
3. Login in the /admin/ area
4. Add the new template in the dashboards area
5. Add the new article in the dashboards area
6. Select the article you want to edit
7. Write in the content areas and save you work
8. Follow the article link to see the final result! :)

## Deploy

* Django changes in the application before deploy [link](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/)
* To deploy the application the django server is not suitable, use something like django + uwsgi + nginx 
[link](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
