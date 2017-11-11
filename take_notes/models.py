from django.db import models

class UserNotes(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(default=0)
    modified_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)

