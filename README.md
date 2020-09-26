# Link Lizard - URL shortening tool

[![Build Status](https://travis-ci.org/pcp11/link-lizard.svg?branch=master)](https://travis-ci.org/github/pcp11/link-lizard)
[![GitHub](https://img.shields.io/github/license/pcp11/link-lizard)](https://github.com/pcp11/link-lizard/blob/master/LICENSE)
[![Deployed on Heroku](https://img.shields.io/badge/heroku-deployed-blueviolet.svg?logo=heroku)](https://lzrd.herokuapp.com/)
[![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/pcp11/link-lizard?logo=python)](https://www.python.org/)
[![djangoversion](https://img.shields.io/badge/django-3.0.7-brightgreen?logo=django)](https://www.djangoproject.com/)
[![bootstrapversion](https://img.shields.io/badge/bootstrap-4.4.1-brightgreen?logo=bootstrap)](https://getbootstrap.com/)

A live deployment is available on Heroku: https://lzrd.herokuapp.com/

## How to run locally

### 1. Install pipenv and go into the shell

```
pip3 install pipenv
pipenv install
pipenv shell
```

### 2. Migrate and run your server

```
./manage.py migrate
./manage.py runserver
```
