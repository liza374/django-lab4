from django.db import models
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(
        'Категорія',
        max_length=250,
        help_text='Максимум 250 символів'
    )
    slug = models.SlugField('Слаг', blank=True)

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def __str__(self):
        return self.category


class Tag(models.Model):
    name = models.CharField(
        'Тег',
        max_length=100,
        unique=True,
        help_text='Введіть назву тегу'
    )
    slug = models.SlugField('Слаг', blank=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=250,
        help_text='Максимум 250 символів'
    )
    description = models.TextField(
        'Опис',
        blank=True
    )
    pub_date = models.DateTimeField(
        'Дата публікації',
        default=timezone.now
    )
    slug = models.SlugField(
        'Слаг',
        unique_for_date='pub_date'
    )
    main_page = models.BooleanField(
        'Головна',
        default=False,
        help_text='Показувати на головній сторінці'
    )
    category = models.ForeignKey(
        Category,
        related_name='articles',
        blank=True,
        null=True,
        verbose_name='Категорія',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='articles',
        blank=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    def __str__(self):
        return self.title
