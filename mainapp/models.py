from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ("math", "Math"),
        ("english", "English"),
        ("science", "Science"),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
