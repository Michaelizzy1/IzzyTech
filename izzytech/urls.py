from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graphics/', views.graphics_page, name='graphics_page'),
    path('web/', views.web, name='web'),
    path('software/', views.software, name='software'),
    path('mobile/', views.mobile, name='mobile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('success/', views.message_alert, name='success'),
    path('courses/', views.courses, name='courses'),
    path('enrol/', views.enrol, name='enrol'),
]