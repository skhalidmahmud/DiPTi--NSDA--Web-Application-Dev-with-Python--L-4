from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def sendMail(req):
    userMail = 'forusetmp@gmail.com'
    send_mail(
        'test send from Django',
        'Hello there, this is a test mail./nDont warry about this.',
        settings.EMAIL_HOST_USER,
        [userMail]
    )
    return render(req, 'sendMail.html')