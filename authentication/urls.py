from django.contrib import admin
from django.urls import include, path
from . import views #включаємо бачення вюшок

urlpatterns = [
    path('', views.home, name="home"),#тут ми просто задаємо шлях який цій функції треба зробити, напрямляємо її, перший аргумент просто вписуємо поновно і його шукає система знов, другий скерує нас у файл і виконає функцію а третій
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),

]