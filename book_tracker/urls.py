from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path("search/", views.book_search, name="book_search"),
    path("add/", views.add_book_to_library, name="add_book_to_library"),
    path('my-library/', views.my_library, name='my_library'),
    path("library/<int:book_id>/", views.book_detail, name="book_detail"),
    path("library/<int:book_id>/edit/", views.edit_book, name="edit_book"),
    path("library/<int:book_id>/delete/", views.delete_book, name="delete_book"),
    path(
        "library/<int:book_id>/rating/update/",
        views.update_book_rating,
        name="update_book_rating"
    ),
    path(
        "library/<int:book_id>/notes/add/",
        views.add_book_note,
        name="add_book_note"
    ),
]