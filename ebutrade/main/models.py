from django.db import models


class APIKeys(models.Model):
    my_api_key = models.CharField('api_key', max_length=100)
    my_api_secret = models.CharField('api_secret', max_length=100)


    def __str__(self):
        return self.my_api_key
