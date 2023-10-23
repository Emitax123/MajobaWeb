from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.login_view, name='login'),
    path('home/', views.principal, name = 'index'),
    path('list/<str:id>/', views.list_view, name = 'list'),
    path('tasks/', views.task_view, name = 'tasks'),
    path('creationtab/<str:id>/', views.creation_view, name = 'create'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('modelview/<int:type>/<int:id>/', views.model_view, name = 'modelView'),
    path('notifications/<int:notiId>/', views.notification_view, name = 'notiView'),
    path('erase/', views.delete_task, name = 'deletetask'),
    path('marcar_notificaciones_vistas/', views.mark_notifi, name ='checkNoti'),
    path('accept_task/<int:valor>/', views.accept_task, name = 'accept_task'),
    path('taskend/<int:id>/', views.taskend, name = 'taskend'),
    path('taskcancel/<int:id>/', views.taskcancel, name = 'taskcancel'),
    path('modification/<int:type>/<int:id>/', views.obj_modification, name = 'modify')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns += (static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
