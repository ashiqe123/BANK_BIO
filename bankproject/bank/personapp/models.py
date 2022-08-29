from django.db import models
from django.template.defaultfilters import default
from multiselectfield import MultiSelectField

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Person(models.Model):
    name = models.CharField(max_length=124)

    ACOUNT= (
        ('SAVINGS ACCOUNT','SAVINGS ACCOUNT'),
        ('CURRENT ACCOUNT', 'CURRENT ACCOUNT'),
        ('NRI ACCOUNT', 'NRI ACCOUNT'),
    )
    type= models.CharField(max_length=100,choices=ACOUNT,blank=True, null=True)
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE '),
        ('OTHERS ', 'OTHERS '),
    )
    gender= models.CharField(max_length=100, choices=GENDER, blank=True, null=True)
    BOOK_CHOICES = (
            ('BANK PASS BOOK', 'BANK PASS BOOK'),
            ('CREDIT CARD', 'CREDIT CARD'),
            ('DEBIT CARD', 'DEBIT CARD'),
            ('CHECKBOOK', 'CHECKBOOK'),
        )

    DOB=models.DateField('DOB(dd/mm/yy)',null=True)
    age=models.IntegerField(default=True)
    gender=models.CharField(max_length=25,choices=GENDER,blank=True, null=True)
    phone_number=models.IntegerField()
    email_id=models.EmailField()
    adress=models.TextField(max_length=500)
    meterial_provided=MultiSelectField(max_length=100,max_choices=4,choices=BOOK_CHOICES,default=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.name)