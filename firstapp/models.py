from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

from django.core.validators import MaxValueValidator
from pygments.lexer import default
from samba.dcerpc.dcerpc import request


class ChaiVriety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('EL', 'Elachi'),
        ('CD', 'Cold'),
        ('ML', 'Masala'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_add = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='No description')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        validators=[MaxValueValidator(500000.00)]  # Set maximum price limit
    )


    def __str__(self):
        return f"{self.name:<20}     {self.get_type_display():<10}     ${self.price:,.2f}"


# One to  many
class Reviews(models.Model):
    chai = models.ForeignKey(ChaiVriety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.username} review for {self.chai.name}"

# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    chai_variety = models.ManyToManyField(ChaiVriety,related_name='store')

def __str__(self):
    return self.name

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVriety,on_delete=CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date= models.DateTimeField(default= timezone.now)
    valid_date = models.DateTimeField()

def __str__(self):
    return f'Certificate for Chai is : {self.name.chai}'