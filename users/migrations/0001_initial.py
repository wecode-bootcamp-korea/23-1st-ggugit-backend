<<<<<<< HEAD
# Generated by Django 3.2.5 on 2021-08-05 16:46
=======
# Generated by Django 3.2.5 on 2021-08-04 14:57
>>>>>>> a7cceedbbb27dea648dc0c2368dd33366330582d

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=45)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
