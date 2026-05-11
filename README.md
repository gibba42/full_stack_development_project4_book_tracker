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

Saved books are shown on the My Library page:

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

## Testing

### Manual Testing

Manual testing was completed against the user stories defined for this project. Each test was designed to check whether the implemented feature met the acceptance criteria described in the relevant GitHub issue.

| Epic | User Story | Acceptance Criteria Tested | Test Steps | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| Epic 1: User Authentication and Account Management | User Story 1.1: Register account | Successful registration | 1. Navigate to the Register page. <br> 2. Enter a valid username. <br> 3. Enter a valid email address. <br> 4. Enter a valid password. <br> 5. Confirm the password. <br> 6. Submit the form. | The account is created successfully. The user is logged in and redirected to the profile/account area. A success message is displayed. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.1: Register account | Unsuccessful or invalid registration | 1. Navigate to the Register page. <br> 2. Submit the form with missing required fields. <br> 3. Repeat using mismatched passwords. <br> 4. Repeat using an invalid email address. | The account is not created. The user remains on the registration page. Form validation errors are displayed explaining what needs to be corrected. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.2: Login | Successful login | 1. Navigate to the Login page. <br> 2. Enter valid login credentials for an existing account. <br> 3. Submit the form. | The user is logged in successfully and redirected to the correct authenticated area. The navigation updates to show authenticated user options such as My Library and Log out. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.2: Login | Unsuccessful login | 1. Navigate to the Login page. <br> 2. Enter an incorrect username and/or password. <br> 3. Submit the form. | The user is not logged in. An error message is displayed explaining that the login details are invalid. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.3: Logout | Successful logout | 1. Log in as a registered user. <br> 2. Click the Log out button in the navigation bar. | The user is logged out. The navigation updates to show logged-out options. The user is redirected away from protected content. | As expected after configuring logout redirect. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.4: Restrict Access to Pages | Logged-in user can access restricted pages | 1. Log in as a registered user. <br> 2. Navigate to My Library. <br> 3. Navigate to the Profile page. <br> 4. Open the detail page for a saved book. | The logged-in user can access their restricted pages and view their own saved data. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.4: Restrict Access to Pages | Logged-out user cannot access restricted pages | 1. Log out. <br> 2. Attempt to access My Library directly by entering the URL. <br> 3. Attempt to access a saved book detail page directly by entering the URL. | The logged-out user is redirected to the login page and cannot view restricted content. | As expected. | Pass |
| Epic 1: User Authentication and Account Management | User Story 1.5: Edit Account Details | Profile update | 1. Log in as a registered user. <br> 2. Navigate to the profile/account area. <br> 3. Attempt to edit account details. | The user should be able to update profile details and see the updated details on the profile page. | This feature was not implemented in the final version. It was treated as a Should-have item and left as a future improvement. | Not Implemented |
| Epic 1: User Authentication and Account Management | User Story 1.6: Password Reset | Reset password request | 1. Navigate to the Login page. <br> 2. Look for a password reset option. <br> 3. Attempt to request a password reset. | The user should receive password reset instructions. | This feature was not implemented in the final version. It was treated as a Could-have item and left as a future improvement. | Not Implemented |
| Epic 2: Book Search and API Integration | User Story 2.1: Search for Books | Book search | 1. Navigate to the Search Books page. <br> 2. Enter a valid book title, such as "The Hobbit". <br> 3. Submit the search form. | A list of books matching the search term is displayed. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.1: Search for Books | Search by author | 1. Navigate to the Search Books page. <br> 2. Enter an author name, such as "J.R.R. Tolkien". <br> 3. Submit the search form. | A list of books linked to the author is displayed. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.2: Display Search Results | Search results displayed | 1. Search for a valid book title. <br> 2. Review the displayed results. | Each result displays key book information, including title and author. Where available, cover images and first publication year are also shown. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.2: Display Search Results | No matching results | 1. Navigate to the Search Books page. <br> 2. Enter a search term unlikely to return results. <br> 3. Submit the search form. | A clear message is displayed explaining that no books matched the search. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.3: Add Book to My Profile | Add book to My Library | 1. Log in as a registered user. <br> 2. Search for a book. <br> 3. Click Add to My Library on one of the search results. | The selected book is saved to the user's personal library. The user receives confirmation that the book was added. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.3: Add Book to My Profile | Logged-out user cannot add book | 1. Log out. <br> 2. Search for a book. <br> 3. Review the search result actions. | The user is not shown the Add to My Library button. Instead, they are prompted to log in before saving books. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.4: Handle API Errors | API request failure | 1. Simulate the Open Library API being unavailable, or temporarily alter the API URL during development testing. <br> 2. Submit a book search. | The application does not crash. A user-friendly error message is shown explaining that book search is currently unavailable. | As expected during development test. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.4: Handle API Errors | API timeout | 1. Simulate a timeout from the Open Library API during development testing. <br> 2. Submit a book search. | The application does not crash. A user-friendly message is shown explaining that the search took too long and the user should try again. | As expected during development test. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.5: Filter and Sort Search Results | Sort by title | 1. Search for a book or author that returns multiple results. <br> 2. Select the Title sort option. <br> 3. Submit the search. | The returned results are sorted alphabetically by title. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.5: Filter and Sort Search Results | Sort by author | 1. Search for a book or author that returns multiple results. <br> 2. Select the Author sort option. <br> 3. Submit the search. | The returned results are sorted alphabetically by author. | As expected. | Pass |
| Epic 2: Book Search and API Integration | User Story 2.5: Filter and Sort Search Results | Filter by cover availability | 1. Search for a book or author that returns multiple results. <br> 2. Select the option to only show books with covers. <br> 3. Submit the search. | Only results with available cover images are displayed. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.1: View My Library | User views saved books | 1. Log in as a registered user. <br> 2. Add at least one book to My Library. <br> 3. Navigate to My Library. | The saved book is displayed in the user's library. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.1: View My Library | Empty library state | 1. Log in as a user with no saved books. <br> 2. Navigate to My Library. | An empty-state message is displayed explaining that the user has not added any books yet. A link is provided to search for books. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.2: Add a Book to My Library | Book added successfully | 1. Log in as a registered user. <br> 2. Search for a book. <br> 3. Click Add to My Library. <br> 4. Navigate to My Library. | A new book record is created and appears in My Library. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.2: Add a Book to My Library | Duplicate book is not added | 1. Log in as a registered user. <br> 2. Add a book to My Library. <br> 3. Search for the same book again. <br> 4. Click Add to My Library again. | A duplicate record is not created. A message informs the user that the book is already in their library. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.3: Edit a Reading Log | Successful edit | 1. Log in as a registered user. <br> 2. Open a saved book from My Library. <br> 3. Edit the saved book details or rating. <br> 4. Submit the form. | The updated information is saved. The user receives confirmation and the updated information is shown in the interface. | As expected for rating updates. Book detail editing should be tested if this feature remains in the final version. | Pass / Review Needed |
| Epic 3: Reading Log and Personal Library | User Story 3.3: Edit a Reading Log | Invalid edit | 1. Log in as a registered user. <br> 2. Open a saved book from My Library. <br> 3. Submit invalid data where validation applies. | The invalid data is not saved. A validation message is shown explaining what needs to be corrected. | As expected for rating validation. Book detail editing should be reviewed depending on final implementation. | Pass / Review Needed |
| Epic 3: Reading Log and Personal Library | User Story 3.4: Delete a Book Log | Confirm deletion | 1. Log in as a registered user. <br> 2. Navigate to My Library. <br> 3. Open a saved book. <br> 4. Click Delete Book. | A confirmation page is displayed asking the user to confirm whether they want to delete the book. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.4: Delete a Book Log | Successful deletion | 1. Log in as a registered user. <br> 2. Open a saved book. <br> 3. Click Delete Book. <br> 4. Confirm deletion. | The book is removed from My Library. A success message confirms that the book was deleted. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.4: Delete a Book Log | Cancel deletion | 1. Log in as a registered user. <br> 2. Open a saved book. <br> 3. Click Delete Book. <br> 4. Click Cancel on the confirmation page. | The book is not deleted. The user is returned to the book detail page. | As expected. | Pass |
| Epic 3: Reading Log and Personal Library | User Story 3.5: Reading Statistics | Statistics displayed | 1. Log in as a user with saved books. <br> 2. Navigate to My Library. <br> 3. Look for reading statistics such as total books, top-rated books or rating summaries. | Reading statistics should be shown on My Library. | This feature was not implemented in the final version. It was treated as a Could-have item and left as a future improvement. | Not Implemented |
| Epic 3: Reading Log and Personal Library | User Story 3.5: Reading Statistics | No books saved | 1. Log in as a user with no saved books. <br> 2. Navigate to My Library. | An empty-state message should be displayed. | Empty-state message is displayed. Statistics were not implemented. | Partial |
| Epic 4: Notes and Writer Analysis | User Story 4.2: Add Notes to a Book | Add notes | 1. Log in as a registered user. <br> 2. Add a book to My Library. <br> 3. Open the saved book detail page. <br> 4. Select a note category. <br> 5. Enter note content. <br> 6. Click Add Note. | The note is saved against the selected book and displayed on the book detail page. | As expected. | Pass |
| Epic 4: Notes and Writer Analysis | User Story 4.2: Add Notes to a Book | Empty note | 1. Log in as a registered user. <br> 2. Open a saved book detail page. <br> 3. Select a note category. <br> 4. Leave the note content empty. <br> 5. Submit the form. | The note is not saved. A message is displayed explaining that notes require content before they can be saved. | As expected. | Pass |
| Epic 4: Notes and Writer Analysis | User Story 4.2: Add Notes to a Book | Categorised notes | 1. Log in as a registered user. <br> 2. Open a saved book detail page. <br> 3. Add notes using different categories, such as General, Themes, Structure, Character Arcs and Personal Reflections. | Notes are saved with the selected category and displayed with the correct category label. | As expected. | Pass |
| Epic 4: Notes and Writer Analysis | User Story 4.2: Add Notes to a Book | Edit existing note | 1. Log in as a registered user. <br> 2. Open a saved book with an existing note. <br> 3. Click Edit Note. <br> 4. Update the category or content. <br> 5. Save the changes. | The note is updated and the new content is displayed on the book detail page. | As expected. | Pass |

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
