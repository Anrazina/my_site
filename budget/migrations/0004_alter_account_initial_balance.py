# Generated by Django 5.0.4 on 2024-05-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_transaction_permanent_alter_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
