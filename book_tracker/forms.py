from django import forms
from .models import Book, BookNote


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


class BookNoteForm(forms.ModelForm):
    class Meta:
        model = BookNote
        fields = ["category", "content"]
        labels = {
            "category": "Note type",
            "content": "Note",
        }
        widgets = {
            "category": forms.Select(),
            "content": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Write your thoughts about this book..."
                }
            )
        }

    def clean_content(self):
        content = self.cleaned_data.get("content", "").strip()

        if not content:
            raise forms.ValidationError(
                "Notes require content before they can be saved."
            )

        return content
