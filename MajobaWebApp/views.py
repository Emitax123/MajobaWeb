from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import Product, Employee, Machine, Notification, Task
from django.contrib.auth.models import User
from .forms import EmployeeForm, UserForm, ProductForm, MachineForm, TaskForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# views.py


    
#Vista principal
@login_required
def principal (request):
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('name')[:4]
        employees = Employee.objects.all().order_by('name')[:5]
        return render(request, 'index.html', { 'products':products , 'empl':employees})

#VIsualizacion de los modelos
'''
  Utilzada en el acceso directo a un modelo,
  las notificaciones tienen su propio visor
'''
@login_required
def model_view(request,type, id):
    if type == 1:#Employee
        obj = Employee.objects.get(pk=id)
        return render (request,'employee_template.html', {'obj':obj})
    if type == 2:#Machine
        obj = Machine.objects.get(pk=id)
        return render (request,'machine_template.html', {'obj':obj})
    if type == 3:#Product
        obj = Product.objects.get(pk=id)
        return render (request,'product_template.html', {'obj':obj})
    if type == 4:#Task
        obj = Task.objects.get(pk=id)
        return render (request,'task_template.html', {'obj':obj})
    

#Visualizacion de notificacions
'''
    Cada notificacion tiene un atributo 'type',
    indica a que tipo de modelo refiere, con esto gestionamos
    el accionar con una cade de if
'''


@login_required
def obj_modification(request, type, id):
    if type == 1:#Employee
        obj = Employee.objects.get(pk=id)
        if request.method == 'POST':
            template = 'employee_template.html'
            form = EmployeeForm (request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return render (request, template, {'obj':obj})
        form = EmployeeForm (instance=obj)
        title = 'Modificar empleado'
    if type == 2:#Machine
        obj = Machine.objects.get(pk=id)
        if request.method == 'POST':
            template = 'machine_template.html'
            form = MachineForm (request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return render (request, template, {'obj':obj})
        form = MachineForm (instance=obj)
        title = 'Modificar vehiculo'
    if type == 3:#Product
        obj = Product.objects.get(pk=id)
        if request.method == 'POST':
            template = 'product_template.html'
            form = ProductForm (request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                return render (request, template, {'obj':obj})
        form = ProductForm (instance=obj)
        title = 'Modificar producto'
    return render(request, 'create_template.html', {'form':form, 'title':title})
    

@login_required
def task_view(request):
    icons = {
    'pdf': 'pdf_icon.png',
    'doc': 'doc_icon.png',
    'txt': 'txt_icon.png',
    }
    tasks = Task.objects.all()
    userid = request.user.id
    return render (request, 'task_template.html', {'tasks':tasks, 'icons':icons, 'userid':userid})

@login_required
def notification_view (request,notiId):
    #marcamos la notificacion como leida
    Notification.objects.filter(pk=notiId).update (is_read = True)
    #Analizmos el type: #1:Employee 2:Machine 3:Product 4:Tarea
    noti = Notification.objects.get(pk=notiId)
    if noti.type == 1: #Empleado
        obj = Employee.objects.get(pk=noti.obj_id)
        return render(request, 'employee_template.html', {'obj':obj, 'id':noti.type})
    if noti.type == 2: #Maquina
        obj = Machine.objects.get(pk=noti.obj_id)
        return render(request, 'notification_preview.html', {'obj':obj, 'id':noti.type})
    if noti.type == 3: #Producto
        obj = Product.objects.get(pk=noti.obj_id)
        return render(request, 'product_template.html', {'obj':obj, 'id':noti.type})
    if noti.type == 4: #Tarea
        obj = Task.objects.get(pk=noti.obj_id)
        return render(request, 'task_template.html', {'obj':obj, 'id':noti.type})


#Lista simple de las notificaciones, solo util para pruebas  
def mark_notifi(request):
    Notification.objects.filter(receive__id__icontains= request.user.id).update (is_check = True)
    response = {
        "message":"la funcion es correcta"
    }
    return JsonResponse(response)

def accept_task(request,valor):
    task = Task.objects.get(pk=valor)
    print("Hola")
    if task.taker == 0:
        print("hola 2")
        task.taker = request.user.id
        task.state = "En proceso"
        task.save()
        response = {"message":"la funcion es correcta"}
    else:
        response = {"message":"Lo sentimos, alguien ya tomo este pedido"}
    return JsonResponse(response)

#Lista simple de los modelos, acciona segun la id recibida mediante la URL
@login_required    
def list_view(request, id):
    if id == 'Empleado':
        lista =  Employee.objects.all().order_by('name')
    elif id == 'Vehiculo':
        lista = Machine.objects.all().order_by('name')
    elif id == 'Producto':
        lista = Product.objects.all().order_by('name')
    elif id == 'Tarea':
        lista = Task.objects.all().order_by('created')
    return render(request, 'list_template.html', {'list':lista , 'id':id}) 


#Formularios de creacion
'''
    Usamos un id por URL para seleccionar que tipo de modelos creamos
    A la vez debemos crear la notificaion correspondiente e indicar su type
'''
@login_required
def creation_view(request, id):
    '''type:1:Employee 2:Machine 3:Product 4:Task'''
    if request.method == 'POST':
        if id == 'Empleado':
            form = EmployeeForm(request.POST, request.FILES)
            type=1 
        elif id == 'Vehiculo':
            form = MachineForm(request.POST)
            type=2
        elif id == 'Producto':
            form = ProductForm(request.POST, request.FILES)
            type=3
        elif id == 'Tarea':
            form = TaskForm( request.POST, request.FILES)
            type=4
        if form.is_valid():
                if type == 4:
                    obj=form.save(commit=False) #Se guarda el objeto y se lo rellaciona a una variable
                    obj.creator = request.user
                    obj.save()
                    obj_id = obj.id
                else:
                    obj=form.save() #Se guarda el objeto y se lo rellaciona a una variable
                    obj_id=obj.id
                create_notification(request, id, obj_id, type)
                if 'save_and_backhome' in request.POST:
                    return redirect('index')
                if 'save_and_return' in request.POST:

                    if id == 'Empleado':
                        form = EmployeeForm() 
                    elif id == 'Vehiculo':
                        form = MachineForm()
                    elif id == 'Producto':
                        form = ProductForm()
                    elif id == 'Tarea':
                        form = TaskForm()
                    return render(request, 'create_template.html', {'form':form, 'id':id})
    else:
        if id == 'Empleado':
            form = EmployeeForm() 
        elif id == 'Vehiculo':
            form = MachineForm()
        elif id == 'Producto':
            form = ProductForm()
        elif id == 'Tarea':
            form = TaskForm()
    return render(request, 'create_template.html', {'form':form, 'id':id})

def delete_task(request):
    Task.objects.all().delete()
    return redirect('index')
def taskcancel(request, id):
    Task.objects.filter(id=id).update(taker=0, state ='Pendiente')
    return redirect('tasks')
def taskend(request, id):
    Task.objects.filter(id=id).update(state ='Terminado')

    return redirect('tasks')
#Logeo de user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir a la página principal después del inicio de sesión exitoso
    else:
        # Si el usuario ya está autenticado, redirigir a la página principal
        if request.user.is_authenticated:
            return redirect('index')
    form = UserForm()
    return render(request, 'user_login.html', {'form':form})


#Manejo de notificaciones
def create_notification(request, id, obj_id, type):
    user = request.user
    if type == 4:
         msg = " ha creado una nueva " + id 
    else:
        msg = " ha creado un nuevo " + id 
    receivers = User.objects.exclude(id=user.id)
    noti = Notification.objects.create(sender=user, obj_id=obj_id, type=type, msg=msg)
    noti.receive.set(receivers) 
    
#Listado simple de notificaiones
@login_required
def notification_list(request):
    notifications = Notification.objects.filter(receive__id__icontains= request.user.id)
    return render(request, 'notifications.html', {'noti':notifications})

#Borra todos los checks de las notificaiones, uso de prubeba solamente
def delete_check(request):
    if request.method == 'POST':
        noti = Notification.objects.filter(receive__id__icontains= request.user.id)
        noti.update(is_check=True)
        cant_noti = (Notification.objects.filter(is_check=False)).count()
        response = {'cant_noti':cant_noti}
        print(cant_noti)
    return JsonResponse(response)
    
#Deslogeo
def logout(request):
    logout(redirect)


#ERRORES 404 y 500 (plantillas personlaizadas)
def error_404(request, exception):
    return render (request, 'error_404.html', status=404)
def error_500(request):
    return render (request, 'error_404.html', status=500)