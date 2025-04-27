from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=110, verbose_name='Пункт меню')
    slug = models.SlugField(max_length=110, unique=True, db_index=True, verbose_name="URL")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родитель')
    menu_type = models.ForeignKey('MenuType', on_delete=models.CASCADE, null=True, verbose_name='Имя меню')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'


class MenuType(models.Model):
    name = models.CharField(max_length=110, verbose_name='Имя меню')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип меню'
        verbose_name_plural = 'Типы меню'
