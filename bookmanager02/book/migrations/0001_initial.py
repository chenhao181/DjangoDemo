# Generated by Django 4.1.7 on 2023-03-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='名字')),
                ('pub_date', models.DateField(null=True)),
                ('readCount', models.IntegerField(default=0)),
                ('commentCount', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '书籍管理',
                'db_table': 'bookinfo',
            },
        ),
    ]
