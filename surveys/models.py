from surveys.managers import SurveyManager
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    start_date = models.DateTimeField(verbose_name="Дата старта", null=True, blank=True)
    end_date = models.DateTimeField(verbose_name="Дата окончания", null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)

    objects = SurveyManager()

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Question(models.Model):
    TYPE_CHOICES = [
        (1, "Text"),
        (2, "Checkbox"),
        (3, "Multicheckbox"),
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Текст вопроса")
    type = models.IntegerField(choices=TYPE_CHOICES)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    user_id = models.PositiveIntegerField("ID пользователя")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(verbose_name="Текст ответа")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

