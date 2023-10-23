from django.contrib import admin
from .models import Category, Product, Machine, Counter, Employee, Notification, Task
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Machine)
admin.site.register(Counter)
admin.site.register(Employee)
admin.site.register(Notification)
admin.site.register(Task)