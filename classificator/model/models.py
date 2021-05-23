from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/image/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)