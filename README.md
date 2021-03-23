# Lab Django with MySQL

This lab runs on the Heroku cloud.
However, it can also be executed locally with some changes described below, using MySQL in a container, but without data persistence.

## Requirements

* Create an account at [heroku.com](https://www.heroku.com/)
* install Heroku CLI

## Heroku CLI

For more information on how to install Heroku see this [link](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), but basically the command below can be used.

```shell
sudo snap install --classic heroku
```

If you need to install the snap, see the official documentation... [snapcraft](https://snapcraft.io/docs/installing-snapd)

After installing the Heroku CLI, run the commands below.:

```shell
heroku login

#replace the project name (django_mysql)
heroku create django_mysql --buildpack heroku/python

git push heroku master

heroku run python manage.py migrate

heroku run python manage.py createsuperuser
```