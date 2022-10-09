from django.db import models


# Create your models here.

class Applicant(models.Model):
    TYPE = (
        ('sat', 'SAT'),
        ('ielts', 'IELTS'),
    )
    first_name = models.CharField(
        max_length=80,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=80,
        verbose_name='Фамилия'
    )
    telegram = models.CharField(
        max_length=50,
        verbose_name='Телеграм номер или username',
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=80,
        verbose_name='Номер телефона'
    )
    course = models.CharField(
        verbose_name='Курс',
        choices=TYPE,
        max_length=25,
        default='sat'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Question(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )

    def __str__(self):
        return f'Вопрос {self.title}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Feedback(models.Model):
    first_name = models.CharField(
        max_length=80,
        verbose_name='Имя',
    )
    telegram = models.CharField(
        max_length=50,
        verbose_name='Телеграм номер или username',
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=80,
        verbose_name='Номер телефона'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f'Обратная связь {self.first_name}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
