# Generated by Django 5.1.2 on 2025-02-16 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cbos', '0001_initial'),
        ('configurations', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_date', models.DateField(verbose_name='Data de Admissão')),
                ('experience_contract_days', models.IntegerField(blank=True, null=True, verbose_name='Nº de Dias em Contrato de Experiência')),
                ('experience_extension_days', models.IntegerField(blank=True, null=True, verbose_name='Nº de Dias de Prorrogação em Contrato de Experiência')),
                ('position_01', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cargo 01')),
                ('position_02', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cargo 02')),
                ('change_date', models.DateField(blank=True, null=True, verbose_name='Data da Alteração')),
                ('salary_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor do Salário')),
                ('monthly_hours', models.IntegerField(verbose_name='Nº de Horas Mensais')),
                ('inclusion_date', models.DateField(verbose_name='Data de Inclusão do Salário')),
                ('agency', models.CharField(blank=True, max_length=10, null=True, verbose_name='Agência')),
                ('account_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nº Conta')),
                ('check_digit', models.CharField(blank=True, max_length=5, null=True, verbose_name='Dígito Verificador')),
                ('operation', models.CharField(blank=True, max_length=10, null=True, verbose_name='Operação')),
                ('pix', models.CharField(blank=True, max_length=50, null=True, verbose_name='PIX')),
                ('dismissal_date', models.DateField(blank=True, null=True, verbose_name='Data de Demissão')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('account_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.accounttype', verbose_name='Tipo de Conta')),
                ('admission_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.admissiontype', verbose_name='Tipo de Admissão')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.bank', verbose_name='Banco')),
                ('cbo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admission_info', to='cbos.cbo', verbose_name='CBO')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admission_info', to='employees.employee', verbose_name='Funcionário')),
                ('harmful_exposure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.harmfulexposure', verbose_name='Exposição a Agentes Nocivos')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.paymenttype', verbose_name='Tipo de Pagamento')),
                ('pix_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.pixtype', verbose_name='Tipo de PIX')),
            ],
            options={
                'verbose_name': 'Informação de Admissão',
                'verbose_name_plural': 'Informações de Admissão',
            },
        ),
    ]
