from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# nenaudojamas
class Task(models.Model):
    name = models.CharField('Task name', max_length=100)
    info = models.CharField('Info', max_length=100)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    date = models.DateField('Date')
    sum = models.IntegerField('Sum')

    def __str__(self):
        return str(self.date)


class Employee(models.Model):
    f_name = models.CharField('First name', max_length=100)
    l_name = models.CharField('Last name', max_length=100)
    job = models.CharField('Job', max_length=100)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Client(models.Model):
    f_name = models.CharField('First name', max_length=100)
    l_name = models.CharField('Last name', max_length=100)
    company = models.CharField('Company', max_length=100)
    contacts = models.CharField('Contacts', max_length=100)
    logo = models.ImageField('Logo', upload_to='logos', null=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Project(models.Model):
    name = models.CharField('Name', max_length=100)
    start_date = models.DateField('Start date')
    end_date = models.DateField('End date')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='projects')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    employees = models.ManyToManyField(Employee, related_name='projects')
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)
    description = HTMLField()
    cover = models.ImageField('Cover', upload_to='covers', null=True)

    def __str__(self):
        return self.name