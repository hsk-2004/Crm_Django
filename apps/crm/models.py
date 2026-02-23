from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Converted', 'Converted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads', null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'email')

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients', null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'email')

    def __str__(self):
        return self.name
