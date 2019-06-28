from django.test import TestCase

from .models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(
            name='Exemple de tâche.',
            description='Description de la tâche',
            creation_date='2019-01-06',
            issue='12345',
            done=False)
        Task.objects.create(
            name='Une autre tâche terminée.',
            description='Description de la tâche',
            creation_date='2019-10-06',
            issue='',
            done=True)
