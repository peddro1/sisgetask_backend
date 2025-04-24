from django.utils import timezone
import uuid
from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('a iniciar', 'A iniciar'),
        ('em andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True, blank=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='a iniciar')
    
    def save(self, *args, **kwargs):
        if self.status == 'finalizada' and not self.end_date:
            self.end_date = timezone.now()
        elif self.status != 'Finalizada':
            self.end_date = None
            
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['start_date']
        # ordering = ['-start_date']
        # ordering = ['-end_date']
        # ordering = ['-status']
        # ordering = ['-name']