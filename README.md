# Book Tracker

ADD MOCKUP IMAGE HERE

Book Tracker is a full-stack reading journal and book analysis application designed for readers, students and aspiring authors.

The application allows users to search for books using the Open Library API, save selected books to a personal library, rate them, and record structured notes. Unlike a simple reading log, Book Tracker is aimed particularly at users who want to analyse books from a writer’s perspective, including themes, structure, character arcs and personal reflections.

This project was built as a data-driven Django application using a PostgreSQL database. It includes user authentication, protected user-owned data, full CRUD functionality and deployment to a cloud platform.

## Live Site

- Live site: ADD HEROKU LINK HERE
- Repository: [GitHub Repository](https://github.com/gibba42/full_stack_development_project4_book_tracker)

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Django
- PostgreSQL
- Open Library API
- Heroku
- Git
- GitHub
- Figma

## Table of Contents

1. [Project Purpose](#project-purpose)
   - [Target Audience](#target-audience)
   - [Project Goals](#project-goals)
   - [User Stories](#user-stories)
2. [Agile Planning](#agile-planning)
   - [Epics](#epics)
   - [User Stories and Acceptance Criteria](#user-stories-and-acceptance-criteria)
   - [MoSCoW Prioritisation](#moscow-prioritisation)
3. [UX Design](#ux-design)
   - [Design Goals](#design-goals)
   - [Wireframes](#wireframes)
   - [Colour Scheme](#colour-scheme)
   - [Typography](#typography)
4. [Features](#features)
5. [Data Model](#data-model)
   - [Entity Relationship Diagram](#entity-relationship-diagram)
   - [User Model](#user-model)
   - [Book Model](#book-model)
   - [Book Note Model](#book-note-model)
6. [Technologies Used](#technologies-used)
7. [Testing](#testing)
   - [Manual Testing](#manual-testing)
   - [User Story Testing](#user-story-testing)
   - [Python Testing](#python-testing)
   - [JavaScript Testing](#javascript-testing)
   - [Validator Testing](#validator-testing)
   - [Responsiveness Testing](#responsiveness-testing)
8. [Bugs](#bugs)
9. [Deployment](#deployment)
10. [Security Features](#security-features)
11. [Credits](#credits)
12. [Future Improvements](#future-improvements)
  
## Project Purpose

The purpose of Book Tracker is to provide a simple, focused tool for recording and analysing books.

Many book tracking tools focus only on whether a user has read a book and what rating they gave it. Book Tracker expands on this by allowing users to record structured notes that are useful for deeper reflection, particularly for aspiring authors who want to learn from the books they read.

The application allows users to:

- Search for books using the Open Library API
- Save books to their own personal library
- Rate saved books
- Add structured notes about each book
- Edit and delete saved book records
- Manage their own data securely through an authenticated account

### Target Audience

Book Tracker is aimed at:

- Readers who want to maintain a personal reading log
- Aspiring authors who want to analyse storytelling techniques
- Students studying literature
- Casual users who want a private record of books they have read

### Project Goals

The main goals of this project are to:

- Build a database-backed Django web application
- Implement user authentication and protected user data
- Allow users to create, read, update and delete their own book records
- Integrate an external API to allow users to search for books
- Provide a clean and responsive user interface
- Use Agile planning to manage the development process
- Deploy the finished application to a cloud platform

## Agile Planning

### User Stories

More detailed User Stories are captured in Github issues, but at a high-level this application aims to meet the following wants:

- As a user, I want to search for books so that I can find titles easily
- As a user, I want to save books so that I can track those I have read
- As a user, I want to rate books so that I can track my opinions on them
- As a user, I want to write notes so that I can analyse books
- As a user, I want to edit or delete entries so that I can manage my data
- As a user, I want to register an account so that my data is secure

## UX Design

### Wireframes

The wireframes for this project were developed using Figma. 

## Features

### Home page

First time users are brought to the home page where they have the options to sign-up, or log in if they already have an account.

![Home page](static/images/README/home-page-example.png)

### Registration page

![Registration page](static/images/README/create-account-example.png)

### Login page

![Log in page](static/images/README/login-example.png)

### My account page

When a user logs in, they are taken to the "My account" page. This page shows a user their user name and email. 

![My account page](static/images/README/my-account-example.png)

###

Any user can search for a book. This feature uses the Open Library API to match search results to a comprehensive list of published books. 

![Book search page](static/images/README/search-book-example-1.png)

If a user is logged in, they are given the option to save books to their library:

![Book search results, user logged in](static/images/README/search-book-example-2.png)

If a user is not logged in, they are shown a message saying they can log in to save books:

![Book search results, user not logged in](static/images/README/search-book-example-3.png)

### My Library page

![My Library page](static/images/README/my-library-example.png)

### Book details and notes

From the My Library page, users can see more details about books they have saved and add a rating:

![Book details page](static/images/README/book-details-example-1.png)

They can also add notes to books, and organise them by different categories:

![Book details page, notes section](static/images/README/book-details-example-2.png)

## Data Model

Book Tracker uses a relational database to store user-owned book records. The application uses Django’s built-in `User` model for authentication and custom models to store books, ratings and notes.

The data model is designed around the core purpose of the application: allowing each registered user to build and manage their own personal reading library.

Each saved book belongs to one user. This ensures that users can only view, edit and delete their own saved books.

### Entity Relationship Diagram

ADD ERD HERE

The database contains the following main relationships:

- A `User` can have many saved `Book` records.
- Each `Book` record belongs to one `User`.
- Each saved `Book` stores information retrieved from the Open Library API, along with user-generated data such as ratings and notes.

### Database Schema

### User Model

This project uses Django’s built-in `User` model.

The `User` model is used to:

- Register new users
- Authenticate login and logout
- Link saved books to the correct user
- Restrict users so they can only access their own saved book records

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key for the user |
| username | CharField | Unique username used to log in |
| password | CharField | Hashed password managed by Django |
| email | EmailField | Optional user email address |
| first_name | CharField | Optional first name |
| last_name | CharField | Optional last name |
| is_active | BooleanField | Identifies whether the user account is active |
| date_joined | DateTimeField | Date and time the user account was created |

### Book Model

The `Book` model stores books saved by users to their personal library.

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key for the saved book record |
| user | ForeignKey | Links the saved book to the logged-in user |
| title | CharField | Stores the title of the book |
| author | CharField | Stores the author of the book |
| open_library_key | CharField | Stores the unique Open Library identifier for the book |
| cover_url | URLField | Stores the URL for the book cover image, where available |
| rating | IntegerField | Stores the user's rating for the book |
| notes | TextField | Stores the user's general notes about the book |
| created_at | DateTimeField | Records when the book was saved |
| updated_at | DateTimeField | Records when the book record was last updated |

### Model Relationship

The relationship between `User` and `Book` is a one-to-many relationship.

One user can save many books, but each saved book belongs to one user.

## Bugs

| Title | Description | Fix | Status |
|-------|-------------|-----|--------|
| Heroku build failing | The project was not building correctly in Heroku, and was showing an "Application Error". | Updated the requirements.txt file based on the build logs to specify the latest version of gunicorn, and added a .python-version file to specify the version of python Heroku should use. | Resolved |
| manage.py runserver command failing due to Post model | The server was unable to run due to an error with the models being imported. | The error was caused by the example blog post model being leftover after the project was changed to a book model. admin.py was updated to reference the correct model. | Resolved |
| manage.py runserver command failing due to delete_book view | The server was unable to run due to the delete_book view not being indented correctly, and the get_object_or_404 shortcut not being imported. | Fixed the indentation issue so that the delete_book view is no longer nested within the edit_book view. Added the get_object_or_404 shortcut to the imports. | Resolved |
| 404 error when rating a book | When a user tries to save a book rating, a 404 error is shown. | The bug was caused by the update_book_rating form not being closed properly. Updated this section so that the form is now correctly actioning. | Resolved |
| Long notes overflowing | If a user adds a very long note, the text overflows the page and shows a horizontal scroll bar. | Updated the base css so that note cards now text wrap on overflow. | Resolved |

## Tutorials and guides used

### Django

This project uses the Django authentication system. This was implemented using the Django documentation:

[Using the Django authentication system](https://docs.djangoproject.com/en/6.0/topics/auth/default/)

To add css styling to the project, I followed this guide:

[How to manage static files in Django](https://docs.djangoproject.com/en/dev/howto/static-files/)

### Open Library

To allow users to search for books, this project uses the Internet Archive's Open Library API. 

[Open Library API](https://openlibrary.org/developers/api)

The book search functionality was built by referencing this documentation:

[Book Search API](https://openlibrary.org/dev/docs/api/search)

ChatGPT was used to help integrate the API with the rest of the project. 
