# Generated by Django 5.1.2 on 2024-11-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0001_initial'),
        ('employees', '0001_initial'),
        ('payroll', '0004_payment_fourth_payment_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pendente'), ('completed', 'Concluído'), ('overdue', 'Atrasado'), ('in_progress', 'Em Andamento')], default='pending', max_length=20, verbose_name='Status'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['status'], name='payroll_pay_status_daa1bd_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['due_date'], name='payroll_pay_due_dat_800aa8_idx'),
        ),
    ]
