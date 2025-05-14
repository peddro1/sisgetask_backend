import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        else:
            self.email = self.username
            
        super(CustomUser, self).save(*args, **kwargs)
        


    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Novo nome para a relação
        blank=True
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Novo nome para a relação inversa
        blank=True
    )
