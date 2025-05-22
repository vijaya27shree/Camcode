# models.py

from django.db import models

class Images(models.Model):
    img_name = models.CharField(max_length=100)
    img_path = models.ImageField(upload_to='images/')
    img_content = models.TextField()

    def __str__(self):
        return self.img_name
