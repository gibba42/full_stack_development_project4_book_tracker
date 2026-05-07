# Book Tracker

A reading journal and analysis tool for aspiring authors. This application allows users to search for books, track what they have read, and record structured notes and ratings. 

This application is built using:

- HTML
- CSS
- JavaScript
- Python with Django framework
- PostgreSQL database
- Open Library API

## Table of Contents

1. [Project Purpose](#project-purpose)
   - Target Audience
   - Project Goals
   - User Stories
2. [Wireframes](]#wireframes)
  
## Project Purpose 

The purpose of this project is to create a **data-driven, full-stack web application** that allows users to manage and analyse their reading habits.

The application enables users to:
- Search for books using an external API
- Save books to their personal library
- Add structured notes and ratings
- Analyse books from a writer’s perspective (themes, structure, character arcs)

### Target Audience

- Readers who want to track books they've read
- Aspiring authors analysing storytelling techniques
- Students studying literature
- Casual users looking for a personal reading log

### Project Goals

- Provide a clean, intuitive UI for managing books
- Implement full CRUD functionality for user-generated content
- Ensure secure authentication and role-based access
- Follow Agile methodology to plan and deliver the application

### User Stories

More detailed User Stories are captured in Github issues, but at a high-level this application aims to meet the following wants:

- As a user, I want to search for books so that I can find titles easily
- As a user, I want to save books so that I can track those I have read
- As a user, I want to rate books so that I can track my opinions on them
- As a user, I want to write notes so that I can analyse books
- As a user, I want to edit or delete entries so that I can manage my data
- As a user, I want to register an account so that my data is secure

## ERD Diagrams

### User model

This project uses Django's build in user model

### Book model

| Key | Title | Type |
|-----|-------|------|

### Book notes

| Key | Title | Type |
|-----|-------|------|

## Wireframes

The wireframes for this project were developed using Figma. 

### Home page

### Registration page

### Login page

### My Library page

## Bugs

| Title | Description | Fix | Status |
|-------|-------------|-----|--------|
| Heroku build failing | The project was not building correctly in Heroku, and was showing an "Application Error". | Updated the requirements.txt file based on the build logs to specify the latest version of gunicorn, and added a .python-version file to specify the version of python Heroku should use. | Resolved |
| manage.py runserver command failing | The server was unable to run due to an error with the models being imported. | The error was caused by the example blog post model being leftover after the project was changed to a book model. admin.py was updated to reference the correct model. | Resolved |

## Tutorials and guides used

### Django

This project uses the Django authentication system. This was implemented using the Django documentation:

[Using the Django authentication system](https://docs.djangoproject.com/en/6.0/topics/auth/default/)

### Open Library

To allow users to search for books, this project uses the Internet Archive's Open Library API. 

[Open Library API](https://openlibrary.org/developers/api)

The book search functionality was built by referencing this documentation:

[Book Search API](https://openlibrary.org/dev/docs/api/search)

ChatGPT was used to help integrate the API with the rest of the project. 
