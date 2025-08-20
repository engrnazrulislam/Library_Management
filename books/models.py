from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13, unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to="books/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.isbn})"
