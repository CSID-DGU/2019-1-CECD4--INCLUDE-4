from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
     path('', views.home, name='home'),
     path('home', views.home, name='home'),
     path('login', views.signin, name='login'),
     path('intro', views.intro, name='intro'),
     path('funding', views.funding, name='funding'),
     path('join', views.join, name='join'),
     path('test', views.test, name='test'),
     path('list', views.list, name='list'),
     path('signup',views.signup,name='signup'),
     path('signout',views.signout,name='signout'),
     path('info/<code>',views.info,name='info'),
     path('register',views.register,name='register'),
     path('connect',views.accountconnect,name='accountconnect'),
     path('listtoken',views.listToken,name='listok'),
     
     path('block',views.blockchain,name='blockchain'),
     path('mypage',views.mypage,name='mypage'),
     path('send/<requestcode>',views.send,name='send'),
     path('sell/<tokenname>',views.sell,name='sell'),
     path('tokenbuying/<code>',views.tokenbuying,name='tokenbuying'),
     path('tokenbuyrequest',views.dbtest,name='tokenbuyrequest'),
     path('finsell',views.finsell,name='finsell'),
     path('tokenregist',views.tokenregis,name='tokenregist'),
     path('adminpage',views.adminpage,name='adminpage'),
     path('statechange/<tokenname>',views.statechange,name='statechange'),
     path('statechangeuser/<tokenname>',views.statechangeuser,name='statechangeuser'),
     path('addwhlist/<companycode>',views.addwhlist,name='addwhlist'),
     path('finapproval',views.finapproval,name='finapproval'),
     path('cantregist', views.tokenregis, name = 'cantregist'), 
 ]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
