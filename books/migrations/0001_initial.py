# Generated by Django 5.0.4 on 2024-05-07 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'book_category',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('price', models.CharField(blank=True, max_length=128)),
                ('year', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book_category')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=256)),
                ('star_given', models.CharField(blank=True, max_length=10)),
                ('user', models.CharField(blank=True, max_length=100)),
                ('bookname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
