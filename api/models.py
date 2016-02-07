from django.db import models


class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks')
    title = models.CharField(max_length=500)
    date = models.DateField(blank=True)

    def __unicode__(self):
        return self.title
