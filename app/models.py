from django.db import models

class ToDo_Model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    details = models.TextField()
    Date = models.DateField()

    def __str__(self):
        return self.title
