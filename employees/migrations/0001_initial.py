# Generated by Django 5.1.2 on 2025-02-16 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0001_initial'),
        ('geography', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome da Mãe')),
                ('father_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Pai')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('pis_nis', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='PIS/NIS')),
                ('military_certificate', models.CharField(blank=True, max_length=20, null=True, verbose_name='Certificado Militar (RA)')),
                ('identity_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número da Identidade (RG)')),
                ('date_emission_identity', models.DateField(blank=True, null=True, verbose_name='Data da Emissão')),
                ('organ_consignor_identity', models.CharField(blank=True, max_length=50, null=True, verbose_name='Orgão Expedidor')),
                ('number_ctps', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número CTPS')),
                ('series_ctps', models.CharField(blank=True, max_length=10, null=True, verbose_name='Série CTPS')),
                ('date_emission_ctps', models.DateField(blank=True, null=True, verbose_name='Data Emissão')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('neighborhood', models.CharField(max_length=50, verbose_name='Bairro')),
                ('number', models.CharField(max_length=10, verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('contact', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('address_uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='geography.state', verbose_name='Estado (UF)')),
                ('city_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='geography.city', verbose_name='Cidade')),
                ('deficiency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurations.deficiency', verbose_name='Deficiência')),
                ('degree_instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.degreeinstruction', verbose_name='Grau de Instrução')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.gender', verbose_name='Genero')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.maritalstatus', verbose_name='Estado Civil')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.nationality', verbose_name='Nacionalidade')),
                ('natural_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naturalidade', to='geography.city', verbose_name='Cidade de Nascimento')),
                ('naturalness_uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naturalidade', to='geography.state', verbose_name='Estado de Nascimento')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.race', verbose_name='Raça')),
                ('uf_ctps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ctps', to='geography.state', verbose_name='Estado de Expedição da CTPS')),
                ('uf_identity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='identidade', to='geography.state', verbose_name='Estado de Expedição')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
