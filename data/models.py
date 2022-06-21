from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField(unique=True, max_length=256)

class ItemType(models.Model):
    name = models.CharField(unique=True, max_length=256)

class AnswerType(models.Model):
    name = models.CharField(unique=True, max_length=256)

class Item(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.CASCADE)

class AnswerOption(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seq_nr = models.IntegerField()
    option_text = models.CharField(max_length=256)

class Statements(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seq_nr = models.IntegerField()
    statement_text = models.CharField(max_length=256)
