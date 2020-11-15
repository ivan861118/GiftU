from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .tasks import send_email_task

def index(request):
    if request.method == 'POST':
        data = request.POST
        send_email_task.delay(recipient=data['recipient'], title=data['title'], message=data['message'])
        return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')
    else:
        return render(request, 'email_service/send_mail.html', locals())
    


        
