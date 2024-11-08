from django.db import models
from geography.models import State, City

class Gender(models.Model):
    description = models.CharField(max_length=20, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.description


class Race(models.Model):
    description = models.CharField(max_length=30, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raça'
        
    def __str__(self):
        return self.description


class MaritalStatus(models.Model):
    description = models.CharField(max_length=20, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'
        
    def __str__(self):
        return self.description


class DegreeInstruction(models.Model):
    description = models.CharField(max_length=30, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Grau de Instrução'
        verbose_name_plural = 'Grau de Instrução'
        
    def __str__(self):
        return self.description


class Deficiency(models.Model):
    description = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Deficiência'
        verbose_name_plural = 'Deficiência'
        
    def __str__(self):
        return self.description


class Nationality(models.Model):
    description = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Nacionalidade'
        verbose_name_plural = 'Nacionalidade'
        
    def __str__(self):
        return self.description


class Employee(models.Model):
    # Dados Pessoais
    full_name = models.CharField(max_length=100, verbose_name='Nome Completo')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Genero')
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name='Raça')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, verbose_name='Estado Civil')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    degree_instruction = models.ForeignKey(DegreeInstruction, on_delete=models.CASCADE, verbose_name='Grau de Instrução')
    deficiency = models.ForeignKey(Deficiency, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Deficiência')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name='Nacionalidade')
    mother_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome da Mãe')
    father_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nome do Pai')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    # Naturalidade
    naturalness_uf = models.ForeignKey(State, related_name='naturalidade', on_delete=models.CASCADE, verbose_name='Estado de Nascimento')
    natural_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='naturalidade', verbose_name='Cidade de Nascimento')

    # Documentos
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    pis_nis = models.CharField(max_length=11, unique=True, blank=True, null=True, verbose_name='PIS/NIS')
    military_certificate = models.CharField(max_length=20, null=True, blank=True, verbose_name='Certificado Militar (RA)')
    identity_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Número da Identidade (RG)')
    data_emission_identity = models.DateField(blank=True, null=True, verbose_name='Data da Emissão')
    organ_expedidor_identidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Orgão Expedidor')
    uf_identity = models.ForeignKey(State, related_name='identidade', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Estado de Expedição')

    # Carteira de Trabalho
    number_ctps = models.CharField(max_length=20, blank=True, null=True, verbose_name='Número CTPS')
    series_ctps = models.CharField(max_length=10, blank=True, null=True, verbose_name='Série CTPS')
    data_emission_ctps = models.DateField(blank=True, null=True, verbose_name='Data Emissão')
    uf_ctps = models.ForeignKey(State, related_name='ctps', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Estado de Expedição da CTPS')

    # Dados complementares
    cep = models.CharField(max_length=10, verbose_name='CEP')
    address_uf = models.ForeignKey(State, related_name='endereco', on_delete=models.CASCADE, verbose_name='Estado (UF)')
    city_address = models.ForeignKey(City, related_name='endereco', on_delete=models.CASCADE, verbose_name='Cidade')
    neighborhood = models.CharField(max_length=50, verbose_name='Bairro')
    number = models.CharField(max_length=10, verbose_name='Número')
    complement = models.CharField(max_length=50, null=True, blank=True, verbose_name='Complemento')

    # Contato
    contact = models.CharField(max_length=15, blank=True, null=True, verbose_name='Contato')
    telephone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.full_name
