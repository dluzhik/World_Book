# Generated by Django 4.1.2 on 2022-12-07 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book'),
        ),
    ]