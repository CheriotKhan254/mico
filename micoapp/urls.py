from django.urls import  path
from . import views
from micoapp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('login/',views.login_view,name='login'),
    path('logout_admin/',views.logout_admin,name='logout.html'),
    path('contact/',views.contact,name='contact.html'),
    path('view_doctor',views.view_doctor,name='view_doctor'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('delete_doctor(?P<int:pid>)',views.delete_doctor,name='delete_doctor'),

    path('view_patient', views.view_doctor, name='view_patient'),
    path('add_patient/', views.add_doctor, name='add_patient'),
    path('delete_patient(?P<int:pid>)', views.delete_patient, name='delete_patient'),

    path('view_appointment', views.view_appointment, name='view_appointment'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)', views.delete_appointment, name='delete_appointment'),

]