from django.db import models
from django.contrib.auth.models import AbstractUser


class Uf(models.Model):
    sigla = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name=("Sigla"))
    nome = models.CharField(max_length=100, verbose_name=('Nome'))

    def __str__(self):
        return '{} {}'.format(self.nome, self.sigla)

    class Meta:
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')

   


class Cidade(models.Model):
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE,
                           null=True, blank=True, verbose_name=('Estado'))
    nome = models.CharField(max_length=100, verbose_name=('Nome'))

    class Meta:
        verbose_name = ('Cidade')
        verbose_name_plural = ('Cidades')

    def __str__(self):
        return '{}/{}'.format(self.name, self.uf)


class Endereco(models.Model):
    cep = models.CharField(
        max_length=100, verbose_name=('CEP'), null=True, blank=True)
    cidade = models.ForeignKey(
        Cidade, on_delete=models.CASCADE, verbose_name=('Cidade'))
    rua = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=('Logradouro'))
    numero = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=('Número'))
    district = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=('Bairro'))
    sem_numero = models.BooleanField(
        default=False, verbose_name=('Sem número'))
    complemento = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=('Complemento'))

    class Meta:
        verbose_name = ('Endereço')
        verbose_name_plural = ('Endereços')

    def __str__(self):
        return '{} - {} - {}'.format(self.zipcode, self.cidade, self.cep)


class Pessoa(AbstractUser):
    nome = models.CharField(max_length=100, verbose_name=('Nome'))
    email = models.EmailField(
        max_length=200, null=True, blank=True, verbose_name=('E-mail'))
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, verbose_name=('Endereço'))
    telefone = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name=('Telefone'))   


    class Meta:
        verbose_name = ('Pessoa')
        verbose_name_plural = ('Pessoas')

    def __str__(self):
        return '{} - {}'.format( self.nome)
