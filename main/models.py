from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=256)
    age=models.IntegerField()
    def __str__(self):
        return self.name
class Article(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    createdAT=models.DateTimeField(auto_now_add=True)
    authors=models.ManyToManyField('Author')
    def __str__(self):
        return self.title