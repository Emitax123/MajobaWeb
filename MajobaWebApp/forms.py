from django import forms
from .models import Category, Employee, Product, Machine, Task
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        #self.label_suffix = ' '
        # Personaliza el placeholder para cada campo
        #self.fields['name'].label = 'sad'
        #self.fields['description'].widget.attrs['placeholder'] = 'asd'

        #for field_name, field in self.fields.items():
            #field.required = False

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        
        fields = {
            'username',
            'password',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['type']
        img = forms.ImageField(widget=forms.FileInput)
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['type']
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = '__all__'
        exclude = ['type']
        
    def __init__(self, *args, **kwargs):
        super(MachineForm, self).__init__(*args, **kwargs)
        conductores = Employee.objects.all()
        options = [(i , i) for i in conductores]
        self.fields['conductor'] = forms.ModelChoiceField(Employee.objects.all())

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['creator', 'state', 'type', 'taker']
        