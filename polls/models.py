import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문내용
    pub_date = models.DateTimeField('date published') #생성날짜

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description = 'Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model): #1대다
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #선택지해당질문, 외래키, question이라는 모델을 참조, cascade
    choice_text = models.CharField(max_length=200) #
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
