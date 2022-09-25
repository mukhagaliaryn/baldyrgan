from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>/', views.subject_detail, name='subject_detail'),
    path('lesson/<slug>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<slug>/tasks/', views.tasks, name='tasks')
]
