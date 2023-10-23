from .models import Notification, Task
def base_context(request):
    if request.user.is_authenticated:
        notifi = Notification.objects.filter(receive__id__icontains= request.user.id).order_by('-created')
        count = (notifi.filter(is_check=False)).count()
        pending_task_count = Task.objects.filter(state__icontains= 'Pendiente').count()
        return {'notifications':notifi, 'count':count, 'pending':pending_task_count}
    else:
        count = 0
        return { 'count':count}