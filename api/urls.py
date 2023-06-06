from . import views
from django.urls import path

urlpatterns = [
    path('getmessages/', views.getmessages, name='getmessages'),
    path('getunseenchat',views.getunseenchat,name='getall'),
    path('getmessages/<str:pk>/', views.getroommessages, name='getroommessages'),
    path('getnotification/<str:pk>/',views.get_unseen_notifiaction , name='get_unseen_notification'),
    path('makeallseennotification/',views.makeallseen,name='makeallseen'),
    path('addmessages/', views.addmessage, name='addmessage'),
    path('getunreadmessages/<str:pk>/',views.getunreadmessages,name='getunreadmessages'),
    path('get_person_unseen_historymessage/',views.get_person_unseen_historymessage,name='get_person_unseen_historymessage'),
]