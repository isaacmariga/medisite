# Generated by Django 4.0.2 on 2022-07-05 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0005_alter_donating_amount_alter_medicine_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.disease'),
        ),
    ]
