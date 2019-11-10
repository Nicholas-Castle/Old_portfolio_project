from django.db import models

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60)
    pub_date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')



