from django.db import models


class Break(models.Model):
    replacement = models.ForeignKey(
        to='breaks.Replacement',
        on_delete=models.CASCADE,
        related_name='breaks',
        verbose_name='Смена',
    )
    member = models.ForeignKey(
        to='breaks.ReplacementMember',
        on_delete=models.CASCADE,
        related_name='breaks',
        verbose_name='Участник смены',
    )
    break_start = models.TimeField(
        verbose_name='Начало обеда',
        null=True,
        blank=True,
    )
    break_end = models.TimeField(
        verbose_name='Конец обеда',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'Обед пользователя {self.member} ({self.pk})'
