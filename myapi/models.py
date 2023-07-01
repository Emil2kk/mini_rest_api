from django.db import models

class Cars(models.Model):
    base=models.CharField( max_length=50)
    motor=models.CharField( max_length=50)
    def __str__(self):
        return self.base + ' ' +self.motor
    