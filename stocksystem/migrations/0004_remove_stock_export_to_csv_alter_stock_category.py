# Generated by Django 4.1.1 on 2022-10-07 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocksystem', '0003_alter_stock_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_csv',
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stocksystem.category'),
        ),
    ]
