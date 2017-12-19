from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)