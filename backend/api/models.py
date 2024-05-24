from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length = 100) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) #don't pass it just populate every instance of note
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "notes") 
    #links a user to the data that is related (one to many relationship)
    #will link to some data source the user, and on delete will delete the note (title, content, created_at) 
    
    def __str__(self):
        return self.title