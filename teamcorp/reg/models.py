from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    
class Register(models.Model):
    full_name = models.CharField(max_length=250)
    NO_OF_CHILDREN = [
        ('1', '1-2'),
        ('2', '2-3'),
        ('3', '3-4'),
        ('4', '4-5'),
        ('5', '5+'),
    ]
    no_of_children = models.CharField(
        max_length=1,
        choices=NO_OF_CHILDREN,
        default='1',
    )
    GUARDIAN_ROLE = [
        ('Guardian', 'Guardian'),
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Grandparent', 'Grandparent'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
    ]
    guardian_role = models.CharField(
        max_length=50,
        choices=GUARDIAN_ROLE,
        default='Guardian',
    )
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER,
        default='Male',
    )
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Register'

    def __str__(self):
        return self.full_name