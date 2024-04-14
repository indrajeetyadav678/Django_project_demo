from django.urls import path
from .views import *

urlpatterns=[
 path('',home, name="index"),
 path('about-us/',about, name="about"),
 path('services/',service,name="service"),
 path('product/',product,name="product"),
 path('contact-us/',contact,name="contact"),
 path('logins/',loginpage,name="login"),
 path('signups/',signuppage,name="signup"),
]