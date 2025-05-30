# Generated by Django 5.2 on 2025-04-27 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tree_menu', '0002_remove_menuitem_test_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110, verbose_name='Имя меню')),
            ],
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_tree_menu.menuitem', verbose_name='Родитель'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_tree_menu.menutype', verbose_name='Имя меню'),
        ),
    ]
