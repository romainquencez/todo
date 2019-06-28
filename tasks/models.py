from django.db import models


class Task(models.Model):
    name = models.CharField('Nom', max_length=500)
    description = models.TextField(blank=True)
    creation_date = models.DateField('Date de création', auto_now=True)
    issue = models.PositiveSmallIntegerField('Numéro de ticket', null=True)
    done = models.BooleanField('Terminé ?', default=False)
