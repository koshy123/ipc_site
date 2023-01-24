from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Recent Date')
    bodytext = models.TextField('Page Info', blank=True)

    def __str__(self):
        return self.title