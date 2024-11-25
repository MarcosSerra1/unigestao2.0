# Generated by Django 5.1.2 on 2024-11-25 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0002_admissioninfo_dismissal_date'),
        ('payroll', '0010_remove_payment_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='bond',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='bond.admissioninfo', verbose_name='Vínculo'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Vencimento'),
        ),
    ]