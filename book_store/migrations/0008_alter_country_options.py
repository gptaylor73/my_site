# Generated by Django 4.2.5 on 2023-09-19 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0007_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]