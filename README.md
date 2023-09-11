# Python project template

This repository contains a template for a python project with clean architecture implemented and configured docker and nginx for deploy.

## Features

- Clean architecture implemented
- Configured docker
- Configured nginx
- DI
- Configured ORM for PostgreSQL with migrations
- All common files
- Configured Flake8
- FastAPI auth (soon)
- React template (soon)

## Tech

This template uses:

- [SQLAlchemy v2.0.17] - ORM
- [FastAPI v0.103.1] - REST API Framework
- [Pydantic v2.3.0] - Data provider
- [Pydantic-settings v2.0.3] - Simple settings (with .env) implementation

## Installation

If you don't need to use SQLAlchemy, then you can simply remove it from the infrastructure and presentation layers.
If you do not need to use FastAPI, then you can remove the api folder from the presentation layer.

## Disclaimer

I'm not claiming that everything is done right here. Perhaps I made a mistake somewhere and something does not work or is not implemented correctly or does not follow the principles of “Clean Architecture”. I'm not forcing you to use this template. I use this template in my projects. This repository is open access because I don't mind sharing any useful information with anyone. I myself once looked for possible implementations of clean architecture in python and found little information that I needed.
### Thank you <3
