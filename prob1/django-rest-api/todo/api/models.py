from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    class Meta:
            ordering = ['-data_created']
            db_table = 'task'
    def __str__(self):
          return self.title