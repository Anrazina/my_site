# Generated by Django 5.0.4 on 2024-05-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='permanent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('I', 'Доход'), ('E', 'Расход'), ('T', 'Перевод')], max_length=1),
        ),
    ]
