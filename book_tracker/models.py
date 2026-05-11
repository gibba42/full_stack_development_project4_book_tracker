from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books"
    )
    open_library_key = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    first_publish_year = models.IntegerField(null=True, blank=True)
    cover_id = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        help_text="Rate this book from 1 to 5."
    )

    class Meta:
        ordering = ["title"]
        # Stops the same book being added twice
        unique_together = ["user", "open_library_key"]

    def __str__(self):
        return f"{self.title} by {self.author}"


class BookNote(models.Model):
    NOTE_CATEGORY_CHOICES = [
        ("general", "General"),
        ("themes", "Themes"),
        ("structure", "Structure"),
        ("character_arcs", "Character Arcs"),
        ("personal_reflections", "Personal Reflections"),
    ]

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    category = models.CharField(
        max_length=30,
        choices=NOTE_CATEGORY_CHOICES,
        default="general"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.get_category_display()} note for {self.book.title}"
