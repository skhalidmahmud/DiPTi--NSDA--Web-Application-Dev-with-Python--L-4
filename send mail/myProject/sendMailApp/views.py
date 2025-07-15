from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import random
from django.core.cache import cache

# Create your views here.
def sendMail(req):
    userMail = 'forusetmp@gmail.com'
    send_mail(
        'Send Mail',
        'Hello there, this is a test mail.' \
        'Dont warry about this.',
        settings.EMAIL_HOST_USER,
        [userMail]
    )
    return redirect('sendMailPage')

def sendMailPage(req):
    return render(req, 'sendMailPage.html')

def forgatePass(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        user = User.objects.get(email=email)
        otp = random.randint(100000, 999999)
        cache.add(email, otp, timeout=60)
        # cache.set(email, otp, timeout=60)  # Use this if you want to overwrite existing OTP
        
        send_mail(
            'OTP for Password Reset',
            f'Your OTP is {otp}',
            settings.EMAIL_HOST_USER,
            [email]
        )

        return render(req, 'otpVerification.html')
    return render(req, 'forgatePass.html')