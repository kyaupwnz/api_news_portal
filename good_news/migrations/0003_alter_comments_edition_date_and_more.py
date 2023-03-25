# Generated by Django 4.1.7 on 2023-03-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_news', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='edition_date',
            field=models.DateTimeField(default=models.DateField(auto_now=True, verbose_name='Дата создания комментария'), verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='edition_date',
            field=models.DateTimeField(default=models.DateField(auto_now=True, verbose_name='Дата создания поста'), verbose_name='Дата изменения'),
        ),
    ]
