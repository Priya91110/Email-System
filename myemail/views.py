from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def mailfun(request):
    if request.method=="POST":
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        messageSent = True
        return render(request,"email_sent.html",{'email':email})

    return render(request,"sendmail.html") 