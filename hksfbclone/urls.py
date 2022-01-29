from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hlo),
    path('login',views.login),
    path('signup',views.signup),
    path('cm',views.cmm),
    path('sgn',views.shsgn),
    path('lgn',views.shlgn),
    path('lgnp',views.shlgn1),
    path('cpost',views.createpost),
    path('logout',views.logout),
    path('addpost',views.addpost),
    path('addcom',views.addcomment),
    path('mposts',views.uposts),
    path('dpost',views.delepost),
    path('dcomme',views.delecomm),
    path('verify/<slug:pid>',views.verify),
    path('verify/verifyacc/<slug:pid>',views.updateuser),
    path('likein',views.likechange),
    path('showprofile',views.yourprofile),
    path('saveupdate',views.saveupdate),
    path('forgetpass/',views.forget_pass),
    path('sendrsetlink/',views.sendrsetlink),
    path('reset/<slug:pid>',views.reset_pass),
    path('reset_done/<slug:pid>',views.reset_done),
    path('emaiverificaton/',views.emaiverificaton),
    path('verifymail',views.verifymail),
    path('Friends/',views.friends)
]
