# Generated by Django 4.0.5 on 2022-06-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_api', '0002_delete_review'),
        ('auth_api', '0004_alter_useraccount_hasread_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='hasRead',
            field=models.ManyToManyField(blank=True, related_name='books_read', to='books_api.book'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='isReading',
            field=models.ManyToManyField(blank=True, related_name='books_reading', to='books_api.book'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='toRead',
            field=models.ManyToManyField(blank=True, related_name='books_wantToRead', to='books_api.book'),
        ),
    ]
