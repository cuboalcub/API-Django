from django.urls import path
import User.View.Login
import User.View.CreateUser
import User.View.hellouser

urlpatterns = [
    path('login', User.View.Login.login),
    path('create', User.View.CreateUser.create_user),
    path('hello', User.View.hellouser.hellouser),
]