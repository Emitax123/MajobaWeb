from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static
# Create your models here.
class Counter(models.Model):
    counter = 0

    @classmethod
    def increment_count():
        counter = counter + 1
    def __str__(self):
        return 'Contador: ' + str(self.counter)


class Category(models.Model):
    type = models.IntegerField(default=0)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripcón')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    type = models.IntegerField(default=3)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(default=0, verbose_name='Stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    img = models.ImageField(upload_to='media/productos/',null=True, default='media/cal.jfif', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    def __str__(self):
        return self.name

def default_image():
    return static('media/img/anonymous.png')

class Employee(models.Model):
    SUCURSAL_CHOICES = (
        ('Castelli', 'Castelli'),
        ('Lezama', 'Lezama')
        )
    type = models.IntegerField(default=1)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    ape = models.CharField(max_length=100, verbose_name='Apellido')
    phone = models.CharField(max_length=20, verbose_name='Telefono')
    mail = models.EmailField(verbose_name='Mail')
    dir = models.CharField(max_length=100, verbose_name='Dirección')
    position = models.CharField(max_length=30, verbose_name='Posición')
    sucursal = models.CharField(max_length=30, choices=SUCURSAL_CHOICES, verbose_name='Sucursal')
    img = models.ImageField(upload_to='media/empleados/', default=default_image, null=True, verbose_name='Fotografia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def __str__(self):
        return self.name
    
class Machine(models.Model):
    state_choices = [
        ('Funcional', 'Funcional'),
        ('No funciona', 'No funciona'),
        ('En reparación', 'En reparaci+on'),
    ]
    type = models.IntegerField(default=2)
    name = models.CharField(max_length=100, verbose_name='Marca')
    patente = models.CharField(max_length=100, verbose_name='Patente')
    state = models.CharField(max_length=100, verbose_name='Estado', choices=state_choices, default='FUncional')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    conductor = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Conductor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
    def __str__(self):
        return self.name


class Notification(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    receive = models.ManyToManyField(User, related_name='receiver_set')
    type = models.IntegerField(default=0)
    obj_id = models.IntegerField(default=0)
    msg = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    is_check = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.sender.username


class Task(models.Model):
    state_choices = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Terminado', 'Terminado'),
    ]
    taker = models.IntegerField(default=0)
    type = models.IntegerField(default=4)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    msg = models.CharField(max_length=50, verbose_name='Indique la tarea a realizar')
    file = models.FileField(upload_to='media/files/', verbose_name='Archivo')
    state = models.CharField(max_length=100, verbose_name='Estado', choices=state_choices, default='Pendiente')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.creator.username
    
