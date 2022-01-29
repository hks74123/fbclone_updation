import email
from typing import MutableSequence
from django.core.checks import messages
from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from hksfbclone.models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from datetime import timezone
import smtplib
import datetime
from email.message import EmailMessage
from random import choice
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def hlo(request):
    if request.user.is_authenticated:
        posts=reversed(item.objects.all())
        dsd=comment.objects.all()
        return render(request,'comm.html',{'psts':posts,'co':dsd})
    else:
        hk=0
        return render(request,'Signup.html',{'hkss':hk})


def generate_random_unicode():
        # logic to generate code
        varsptoken = ''
        alphas = ['-', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(26):
            alphas.append(chr(65+i))
            alphas.append(chr(97+i))
        for i in range(89):
            varsptoken += choice(alphas)

        return varsptoken

def send_mail(to, personalcode):
        # logic to send mail to user
    sender_mail = f"{settings.MAIL_SENDER}"
    password_sender = f"{settings.PASS_MAIL}"
    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome to Fb Clone"
    message.set_content(
        f"Hello User welcome to FbClone.com Your one time login link is\n {settings.SITE_URL}/verify/{personalcode} \nvalid for next 15 minutes.")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return True         # success 
    except:
        return False   

def send_mail1(to, personalcode):
        # logic to send mail to user
    sender_mail = f"{settings.MAIL_SENDER}"
    password_sender = f"{settings.PASS_MAIL}"
    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome to Fb Clone"
    message.set_content(
        f"Hello User welcome to FbClone.com Your Password reset link is\n {settings.SITE_URL}/reset/{personalcode} \nvalid for next 15 minutes.")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_mail, password_sender)
        server.send_message(message)
        return True         
    except:
        return False   

@csrf_exempt
def signup(request):
    if request.method=='POST':
        data = json.loads(request.body)
        first_name= data.get("fname")
        last_name= data.get("lname")
        username= data.get("username")
        email= data.get("email")
        passw= data.get("pass")
        passw1= data.get("pass1")

        if(first_name=='' or last_name=='' or username=='' or email=='' or passw==''):
            return JsonResponse({'status':400,'message':'Please fill out all the fields!!'})

        if passw==passw1:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status':400,'message':'Username aleady exists!!'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'status':400,'message':'Email already exists!!'})
            else:
                personalcode = generate_random_unicode()
                mytimecalculator = 0
                while(len(profile_details.objects.filter(unicode=personalcode))):
                    personalcode = generate_random_unicode()
                    mytimecalculator += 1
                    if mytimecalculator > 10000:
                        pass 

                status = send_mail(email, personalcode)
                user=User.objects.create_user(username=username, password=passw, email=email, first_name=first_name,last_name=last_name)
                user.save();
                hkk=1
                upes = profile_details(user=user, terimail=email,u_nm= username,fstname=first_name,secname=last_name,
                            unicode=personalcode, timestamp=datetime.datetime.now(timezone.utc))
                upes.save()
                return JsonResponse({'status':200,'message':'Verification link has been sent to your email please check inbox!!'})
        else:
            return JsonResponse({'status':400,'message':'Password did not matched !!'})
    else:
        return JsonResponse({'status':400,'message':''})

@csrf_exempt
def login(request):
    if request.method=='POST':
        data = json.loads(request.body)
        username= data.get("username")
        password= data.get("pass")

        if(username=='' or password==''):
            return JsonResponse({'status':400,'message':'Please fill out all fields !!'})
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            datas = profile_details.objects.filter(user=user)
            for data in datas:
                if not data.verified:
                    return JsonResponse({'status':400,'message':'Your mail is not verified...'})
            auth.login(request,user)
            return JsonResponse({'status':200,'message':'success'})
        else:
            return JsonResponse({'status':400,'message':'User does not exists !!'})
    else:
        return render(request,'Signup.html')


def cmm(request):
    posts=reversed(item.objects.all())
    dsd=comment.objects.all()
    return render(request,'comm.html',{'psts':posts,'co':dsd})

def shsgn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        hk=0
        return render(request,'Signup.html', {'hkss':hk})

def shlgn(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        hk=1
        return render(request,'Signup.html', {'hkss':hk})

def shlgn1(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        hk=1
        messages.info(request,'Verification link has been sent to your email please check inbox!!')
        return render(request,'Signup.html', {'hkss':hk})

def createpost(request):
    if request.user.is_authenticated:
        tm=datetime.datetime.now().strftime('%Y-%m-%d ,%H:%M')
        return render(request,'createpost.html',{'times':tm})
    hk=0
    return redirect('/',{'hkss':hk})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        hk=0
        return redirect('/',{'hkss':hk})
    messages.info(request,'Need to login first')
    return render(request,'Signup.html')

@csrf_exempt
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            pos=item()
            pos.username=request.user.username
            pos.time_creat=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            pos.about=request.POST.get('aboutde')
            if len(request.FILES)!=0:
                pos.img=request.FILES['imgle']
            
            dkc=profile_details.objects.get(u_nm=request.user.username)
            pos.author=request.user
            dff=dkc.id
            pos.profile=dkc
            pos.save();
            posts=reversed(item.objects.all())
            return render(request,'comm.html',{'psts':posts})

        return render(request,'createpost.html')
    return render(request,'Signup.html') 


def addcomment(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            dd=request.POST.get('idele')
            ac=comment()
            ac.pst=item.objects.filter(id=dd)[0]
            ac.nam=request.user.username
            ac.body=request.POST.get('hereis')
            ac.save();
            posts=reversed(item.objects.all())
            return render(request,'comm.html',{'psts':posts})
    messages.info(request,'Need to login First')
    return render(request,'Signup.html')  


def uposts(request):
    if request.user.is_authenticated:
        posts=reversed(item.objects.filter(username=request.user.username))
        l=len(item.objects.filter(username=request.user.username))
        dxx=1
        return render(request,'comm.html',{'psts':posts, 'le':dxx, 'lnt':l}) 
    return render(request,'Signup.html')


def delepost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            dde=request.POST.get('idele')
            item.objects.filter(id=dde).delete()
            comment.objects.filter(pst=dde).delete()
            posts=reversed(item.objects.filter(username=request.user.username))
            l=len(item.objects.filter(username=request.user.username))
            dxx=1
            return render(request,'comm.html',{'psts':posts, 'le':dxx, 'lnt':l})
    return render(request,'Signup.html') 


def delecomm(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            ddex=request.POST.get('idele') 
            comment.objects.filter(id=ddex).delete()
            posts=reversed(item.objects.all()) 
            return render(request,'comm.html',{'psts':posts})
    return render(request,'Signup.html')
            

def verify(request, pid):
    return render(request, 'verify.html', {'pid': pid})  


def updateuser(request,pid):
    if request.method == 'POST':
        username = request.POST['unamm']
        me = profile_details.objects.filter(unicode=pid)
        puser = User.objects.filter(username=username)
        if len(me) != 1 or len(puser) != 1:
            return HttpResponse({'user not exists'})
        for person in me:
            if person.verified == 0:
                # match timestamp code here
                cur_time = datetime.datetime.now(timezone.utc)
                pre_time = person.timestamp
                del_time = str(cur_time-pre_time)
                del_time = del_time.split(':')
                if del_time[0] != '0':
                    # delete entry from database
                    profile_details.objects.filter(
                        unicode=pid).delete()
                    User.objects.filter(username=username).delete()
                    return HttpResponse({'Time Limit Exceed'})
                elif int(del_time[1]) > 14:     # 15 minutes time
                    # delete entry from database
                    profile_details.objects.filter(
                        unicode=pid).delete()
                    User.objects.filter(username=username).delete()
                    return HttpResponse({'Time limit Excced'})
                person.verified = 1
                person.unicode = None
                person.save()
                return HttpResponse({'success'})
            else:
                return HttpResponse({'Already Verified.'})
    elif request.user.is_authenticated:
        return redirect('/')
    else:
        return HttpResponse({'user is not authenticated.'})


def likechange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            dd=request.POST.get('idele')
            post=item.objects.get(id=dd)
            user=request.user
            if user in post.liked.all():
                post.liked.remove(user)
            else:
                post.liked.add(user)

            like,created=likes.objects.get_or_create(user=user,post=post)
            if not created:
                if like.value=='Like':
                    like.value=='Unlike'
                else:
                    like.value=='Like'

            like.save()
            return redirect('/')
    messages.info(request,'Need to login first')
    return render(request,'Signup.html')
            
def yourprofile(request):
    if request.user.is_authenticated:
        psd=profile_details.objects.filter(u_nm=request.user.username)
        return render(request,'profile.html',{'prfde':psd})
    return render(request,'Signup.html')

def saveupdate(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            dsdd=profile_details.objects.get(u_nm=request.user.username)
            if len(request.FILES)!=0:
                if len(dsdd.imgp)>0:
                    os.remove(dsdd.imgp.path)
                dsdd.imgp=request.FILES['imgle']
            dsdd.fstname=request.POST.get('f_name')
            dsdd.secname=request.POST.get('l_name')
            dsdd.fbacc=request.POST.get('mmail')
            dsdd.save()
            return redirect('/showprofile')
    return redirect('/')


def forget_pass(request):
    return render(request,'fg.html')

def sendrsetlink(request):
    if request.method=='POST':
        email=request.POST['umail']
        u_obj=User.objects.filter(email=email)
        if u_obj is None:
            messages.info(request,'Emai is not resitered')
            return render(request,'Singup.html')
        else:
            datas = profile_details.objects.filter(terimail=email) 
            for data in datas:
                if not data.verified:
                    messages.info(request,'Username does not exist')
                    return redirect('/sgn')
                personal_code=generate_random_unicode()
                data.unicode=personal_code
                data.save()
                status=send_mail1(email,personal_code)
                messages.info(request,'Password-Reset Link has been sent to your email')
                return redirect('/lgn')

def reset_pass(request,pid):
    return render(request,'rep.html',{'pid':pid})

def reset_done(request,pid):
    if request.method=='POST':
        n_p=request.POST['passtk']
        na_p=request.POST['cpass']
        p_obj=profile_details.objects.filter(unicode=pid)
        for p_obj1 in p_obj:
            u_nam=p_obj1.u_nm
        u_obj=User.objects.filter(username=u_nam)
        if(n_p!=na_p):
            messages.info(request,'Password does not match')
            return redirect(f'/reset/{pid}')
        for u_ob in u_obj:
            u_ob.set_password(n_p)
            u_ob.save()
        for ab in p_obj:
            ab.unicode=None
            ab.save()
        messages.info(request,'Password changed successfully!!')
        return redirect('/lgn') 
    return render(request,'rep.html', {'pid': pid})


def emaiverificaton(request):
    return render(request,'verifymail.html')

@csrf_exempt
def verifymail(request):
    if request.method=='POST':
        data = json.loads(request.body)
        username= data.get("username")
        password= data.get("pass")
        email=data.get("email")
        if(username=='' or password=='' or email==''):
            return JsonResponse({'status':400,'message':'Please fill out all the fields!!'})
        user=auth.authenticate(username=username,password=password)
        data=profile_details.objects.filter(u_nm=username)
        if user is not None:
            for de in data:
                maild=de.terimail
                dsdd=de.verified
                tstamp=de.timestamp
            if(email==maild and dsdd==False):
                cur_time = datetime.datetime.now(timezone.utc)
                del_time = str(cur_time-tstamp)
                del_time = del_time.split(':')
                if int(del_time[1] and del_time[0]==0)<= 14:
                    return JsonResponse({'status':400,'message':'Verification link already sent please check your mail !!'})
                personalcode = generate_random_unicode()
                mytimecalculator = 0
                while(len(profile_details.objects.filter(unicode=personalcode))):
                    personalcode = generate_random_unicode()
                    mytimecalculator += 1
                    if mytimecalculator > 10000:
                        pass 
                for dd in data:
                    dd.timestamp=datetime.datetime.now(timezone.utc)
                    dd.unicode=personalcode
                    dd.save()
                status = send_mail(email, personalcode)
                return JsonResponse({'status':200,'message':'Verification link has been sent to your email please check inbox!!'})
            elif(email!=maild and dsdd==False):
                return JsonResponse({'status':400,'message':'Please enter the registred mail id!!'})  
            elif(email!=maild and dsdd==True):
                return JsonResponse({'status':400,'message':'Please enter the registred mail id which is already verified!!'})
            else:
                return JsonResponse({'status':400,'message':'You email is already verified!!'})
        elif(data is not None):
            return JsonResponse({'status':400,'message':'Password is incorrect !!'})
        
        else:
            return JsonResponse({'status':400,'message':'User does not exist'})
    else:
        return HttpResponse('You are not allowed!!')

def friends(request):
    if request.user.is_authenticated:
        all_users=profile_details.objects.exclude(user=request.user)
        return render(request,'users.html',{'users':all_users})
    else:
        all_users=profile_details.objects.all()
        return render(request,'users.html',{'users':all_users})