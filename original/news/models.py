from django.db import models


class News(models.Model):
    img = models.ImageField(upload_to='news/', blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "New"

