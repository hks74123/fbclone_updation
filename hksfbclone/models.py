from pyexpat import model
from sqlite3 import Timestamp
from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, TimeField
import datetime
# Create your models here.
import os
from django.contrib.auth.models import User

# def filepath(request, filename):
#     old_filename=filename
#     timenow=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     filename='%s%s' % (timenow,old_filename)
#     return os.path.join('static/media/uploads/',filename)



# def filepath1(request, filename):
#     old_filename=filename
#     timenow=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     filename='%s%s' % (timenow,old_filename)
#     return os.path.join('static/media/profile_pics/',filename) 


class profile_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imgp=models.FileField(upload_to='imgs',default='default.jpg', null=True,blank=True)
    u_nm=models.CharField(max_length=150)
    fstname=models.CharField(max_length=250)
    secname=models.CharField(max_length=250)
    terimail=models.EmailField()
    fbacc=models.CharField(max_length=250)
    unicode = models.CharField(max_length=100,null=True)
    timestamp = models.DateTimeField(null=True)
    verified = models.BooleanField(default=False)
    friends=models.ManyToManyField(User,related_name='Friends',blank=True)

class item(models.Model): 
    username=models.CharField(max_length=150)
    time_creat=models.DateTimeField(auto_now_add=True)
    about=models.TextField()
    img=models.FileField(upload_to='imgs', null=True,blank=True)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    profile=models.ForeignKey(profile_details,on_delete=models.CASCADE,related_name='profile')
    @property
    def num_likes(self):
        return self.liked.all().count


LIKE_CHOICE=[
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
]

class likes(models.Model):
    post=models.ForeignKey(item,related_name='like',on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=CASCADE)
    value=models.CharField(choices=LIKE_CHOICE,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)


class total_likes(models.Model):
    post=models.ForeignKey(item,related_name='likesno',on_delete=CASCADE)
    likesss=IntegerField(default=0)


class comment(models.Model):
    pst=models.ForeignKey(item,related_name="comments",on_delete=models.CASCADE)
    nam=models.CharField(max_length=250)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return '%s - %s' % (self.pst.username,self.pst.time_creat)


class friend_request(models.Model):
    from_user=models.OneToOneField(profile_details,related_name='from_user',on_delete=models.CASCADE)
    to_user=models.OneToOneField(profile_details,related_name='to_user',on_delete=models.CASCADE)

class Chat_Groups(models.Model):
    imgp=models.FileField(upload_to='imgs',default='default.jpg', null=True,blank=True) 
    name=models.CharField(max_length=50)
    members=models.IntegerField()
    user=models.ManyToManyField(profile_details)
    admin=models.ManyToManyField(profile_details,related_name='admin',blank=True)
    is_private = models.BooleanField(default=False)
    timestamp = models.DateTimeField(null=True)
    groupcode = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return(self.name)

class Chat(models.Model):
    user=models.ForeignKey(profile_details,on_delete=models.CASCADE)
    group=models.ForeignKey(Chat_Groups,on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField(null=True)

    def __str__(self):
        return(self.message)

class group_request(models.Model):
    group=models.OneToOneField(Chat_Groups,related_name='group',on_delete=models.CASCADE)
    from_pro=models.OneToOneField(profile_details,related_name='from_pro',on_delete=models.CASCADE,null=True)
    to_pro=models.ManyToManyField(profile_details,related_name='to_pro')

    def __str__(self):
        return(self.group.name)
