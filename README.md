# Archived and abaddoned

But you can still review the codebase if needed.

# Snipetto service 

Simple service for storing code snippets.

## Build

| Build  | Status  | 
|---|---|
| CircleCI  | [![CircleCI](https://circleci.com/gh/opalczynski/snippetto_service/tree/master.svg?style=svg)](https://circleci.com/gh/opalczynski/snipetto_service/tree/master) |


## Overview

Snippetto service born from a need to have tooling to collect and search for 
snippets. It works well with [snippetto CLI](https://github.com/opalczynski/snippetto_cli).
Read the `README.md` there too.

Main idea was to bring the process of building snippets base to the terminal. 

I have also an issues that most of the current market solutions by default make
snippets public - which is not always desirable. 

Also noticed that after couple of years of coding - in most cases I am just looking
for code in previous projects - I wanted to make this search process simpler. 


## Stack

Snipetto service is build using:

* [UWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
* [django](https://www.djangoproject.com/)
* [django-rest-framework](https://www.django-rest-framework.org/)
* [django-filter](https://django-filter.readthedocs.io/en/master/)
 

## API documentation

Will be released soon.

## Setup

Current setup is dumb simple.

It is django application with sqlite3 database. You can install it anywhere you
like or join my `small` server - read the CLI `README.md` :) 

To get more insight, take a look at docker-compose file:

    version: '3.7'
    services:
      snipetto-api:
        build:
          context: .
          target: "application"
        ports:
          - "8000:8000"
        volumes:
          - .:/app/
        environment:
          - ENVIRONMENT=development
          - DJANGO_SETTINGS_MODULE=settings.development


## Notes

> Current setup uses sqlite3 - this will be changed to support postgresql and 
mysql too. For now - be careful and mount the volume for the sqlite3 file to 
avoid loosing data.

> I will have a dedicated server used for snippetto - you can join or setup
your own infrastructure.
