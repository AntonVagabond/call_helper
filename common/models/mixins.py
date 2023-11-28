from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from crum import get_current_user

User = get_user_model()


class BaseDictModelMixin(models.Model):
    code = models.CharField(
        'Код',
        max_length=16,
        primary_key=True,
    )
    name = models.CharField(
        'Название',
        max_length=32,
    )
    sort = models.PositiveSmallIntegerField(
        verbose_name='Сортировка',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='Активность',
        default=True,
    )
    color = models.CharField('Цвет', max_length=12, default='#BDECB6')

    class Meta:
        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code} ({self.name})'


class DateMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Created at',
        null=True,
        blank=False,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        null=True,
        blank=False,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)


class InfoMixin(DateMixin):
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='created_%(app_label)s_%(class)s',
        verbose_name='Created by',
        null=True,
    )
    updated_by = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='updated_%(app_label)s_%(class)s',
        verbose_name='Updated by',
        null=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()

        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)
