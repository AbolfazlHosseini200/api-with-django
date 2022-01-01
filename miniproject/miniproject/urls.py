from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('insurance/', views.Insurance.as_view()),
    path('logout/', views.Logout.as_view()),
]
