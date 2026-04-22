from django.db import models

class Property(models.Model):
    PROPERTY_TYPE = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='properties/', null=True, blank=True)

    def __str__(self):
        return self.title