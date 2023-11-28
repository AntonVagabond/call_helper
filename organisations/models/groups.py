from django.db import models
from django.utils import timezone

from common.models.mixins import InfoMixin
from organisations.managers.groups import GroupManager


class Group(InfoMixin):
    organisation = models.ForeignKey(
        to='Organisation',
        on_delete=models.RESTRICT,
        related_name='groups',
        verbose_name='Организация',
    )
    name = models.CharField(
        'Название',
        max_length=255,
    )
    manager = models.ForeignKey(
        to='Employee',
        on_delete=models.RESTRICT,
        related_name='groups_managers',
        verbose_name='Менеджер',
    )
    members = models.ManyToManyField(
        to='Employee',
        related_name='groups_members',
        verbose_name='Участники группы',
        blank=True,
        through='Member',
    )

    objects = GroupManager()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.pk})'


class Member(models.Model):
    group = models.ForeignKey(
        to='Group',
        on_delete=models.CASCADE,
        related_name='members_info',
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.CASCADE,
        related_name='groups_info',
    )
    date_joined = models.DateField(
        verbose_name='Date joined',
        default=timezone.now,
    )

    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'Участники групп'
        ordering = ('-date_joined',)
        unique_together = (('group', 'employee'),)

    def __str__(self):
        return f'Employee {self.employee}'
