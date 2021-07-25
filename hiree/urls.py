from django.contrib import admin
from django.urls import path
from . import views


app_name='hiree'

urlpatterns = [
    path("",views.signup,name="signup"),
    path("signin/", views.signin, name="signin"),
    path("info/",views.info,name="info"),
    path("skills/",views.skills,name="skills"),
    path("profile/",views.profile,name="profile"),
    path("thankyou/",views.thankyou,name="thankyou"),
    path("logout/",views.logout_view  ,name="logout_view"),




]