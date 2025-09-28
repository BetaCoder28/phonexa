from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Manager personalizado para el modelo User"""
    
    def create_user(self, email, password=None, **extra_fields):
        """Crear y retornar un usuario con email y contraseña"""
        if not email:
            raise ValueError('El campo email es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """Crear y retornar un superusuario con email y contraseña"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Contraseña")
    isPremiumUser = models.BooleanField(default=False, verbose_name="Usuario Premium")
    
    # Usar email como campo de autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    # Usar el manager personalizado
    objects = UserManager()
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "users_user"
    
    def __str__(self):
        return f"{self.name} ({self.email})"
