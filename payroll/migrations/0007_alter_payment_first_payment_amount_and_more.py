# Generated by Django 5.1.2 on 2024-11-24 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_alter_payment_first_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='first_payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor do Primeiro Pagamento Parcial'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='fourth_payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor do Quarto Pagamento Parcial'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='second_payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor do Segundo Pagamento Parcial'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='third_payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor do Terceiro Pagamento Parcial'),
        ),
    ]
