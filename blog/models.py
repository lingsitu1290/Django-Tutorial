from django.db import models
from django.utils import timezone

# Defines model object 
# models.Model means the post is a Django Model 
# so Django knows it should be saved in a database

class Post(models.Model):
    # ForeignKey is a link to another model
    author = models.ForeignKey('auth.User')
    # models.CharField text with a limited number of characters 
    title = models.CharField(max_length=200)
    # models.TextField for the long text without a limit
    text = models.TextField()
    # models.DateTimeField is date and time
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Publish method 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Get a text(string) with post title 
    def __str__(self):
        return self.title