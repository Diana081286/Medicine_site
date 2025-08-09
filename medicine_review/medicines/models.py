from django.db import models
from django.contrib.auth.models import User


class Medicine(models.Model):
    name = models.CharField('Наименование', max_length=100)
    description = models.TextField('Описание')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
