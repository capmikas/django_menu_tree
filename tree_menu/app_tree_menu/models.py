from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=110, verbose_name='Пункт меню')
    slug = models.SlugField(max_length=110, unique=True, db_index=True, verbose_name="URL")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name='Родитель')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Элементы меню'
        verbose_name_plural = 'Элементы меню'
