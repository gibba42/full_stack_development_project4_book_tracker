from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "first_publish_year",
            "isbn",
        ]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["rating"]
        widgets = {
            "rating": forms.Select(
                choices=[
                    ("", "No rating"),
                    (1, "1 - Poor"),
                    (2, "2 - Ok"),
                    (3, "3 - Good"),
                    (4, "4 - Very good"),
                    (5, "5 - Excellent"),
                ]
            )
        }