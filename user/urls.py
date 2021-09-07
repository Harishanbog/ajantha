from django.urls import path
from .views import signup,login,home,create_travel
app_name="user"
urlpatterns=[
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('home/',home,name="home"),
    path('create_travel/',create_travel,name="create_travel")

]
