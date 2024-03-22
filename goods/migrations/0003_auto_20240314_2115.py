# Generated by Django 3.2.25 on 2024-03-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20240314_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='good',
            name='categories',
            field=models.ManyToManyField(related_name='goods', to='goods.Category', verbose_name='Категории'),
        ),
    ]
