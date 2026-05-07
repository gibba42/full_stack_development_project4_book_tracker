from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        ordering = ["title"]
        # Stops the same book being added twice
        unique_together = ["user", "open_library_key"]

    def __str__(self):
        return f"{self.title} by {self.author}"
