from django.db import models


# Create your models here.
class Survey(models.Model):
    name = models.CharField(unique=True, max_length=256)

    class Meta:
        db_table = 'surveys'


class ItemType(models.Model):
    name = models.CharField(unique=True, max_length=256)
    has_options = models.BooleanField(default=False)
    has_statements = models.BooleanField(default=False)

    class Meta:
        db_table = 'item_types'


class AnswerType(models.Model):
    name = models.CharField(unique=True, max_length=256)

    class Meta:
        db_table = 'answer_types'


class Item(models.Model):
    # TODO: remove survey when routing is ready
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.CASCADE)
    # TODO: remove seq_nr when routing is ready
    seq_nr = models.IntegerField()
    item_text = models.TextField(max_length=4000)
    display_direction = models.CharField(max_length=10, null=True, blank=True)
    add_text_box_other = models.BooleanField(default=False)
    # TODO: remove page_nr when routing is ready
    page_nr = models.IntegerField()
    # TODO: remove next_page when routing is ready
    next_page = models.IntegerField()
    spss_variable = models.CharField(max_length=32)
    spss_variable_label = models.CharField(max_length=256)
    spss_missing_value = models.CharField(max_length=16)
    spss_format = models.CharField(max_length=16)

    class Meta:
        db_table = 'items'


class ItemOption(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seq_nr = models.IntegerField()
    option_text = models.CharField(max_length=256)
    # TODO: remove next_page when routing is ready
    next_page = models.IntegerField()
    spss_value_label = models.CharField(max_length=256)

    class Meta:
        db_table = 'item_options'


class ItemStatement(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seq_nr = models.IntegerField()
    statement_text = models.CharField(max_length=256)
    spss_variable = models.CharField(max_length=32)
    spss_variable_label = models.CharField(max_length=256)
    spss_missing_value = models.CharField(max_length=16)
    spss_format = models.CharField(max_length=16)

    class Meta:
        db_table = 'item_statements'
