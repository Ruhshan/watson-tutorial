from django.db import models

# Create your models here.
class Blogger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    handle = models.CharField(max_length=20)
    joined = models.DateField()
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.handle

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summery = models.CharField(max_length=300)
    content = models.TextField()
    created_by = models.ForeignKey(Blogger)
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    is_draft = models.BooleanField(default=1)

    def __str__(self):
        return str(self.id)


