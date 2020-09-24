from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Category(models.Model):
    category = models.CharField(max_length=150, verbose_name='categoria')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['id']


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres', default='Sin Nombre')
    DNI = models.CharField(max_length=10, verbose_name='DI', unique=True)
    type = models.ForeignKey(Type,on_delete=models.SET_NULL,related_name='type', null=True, blank=True)
    emp_category = models.ManyToManyField(Category)
    date_joined = models.DateTimeField(auto_created=True, verbose_name='Fecha Creacion')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='modified')
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
