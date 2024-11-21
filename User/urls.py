from django.urls import path
import User.View.Login
import User.View.CreateUser
import User.View.hellouser
import User.View.logout

urlpatterns = [
    path('login', User.View.Login.login),
    path('signup', User.View.CreateUser.create_user),
    path('hello', User.View.hellouser.hellouser),
    path('logout', User.View.logout.logout),
]