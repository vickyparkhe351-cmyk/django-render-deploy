from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name="home"),
    path("about",views.about, name="about"),
    path("service",views.service, name="service"),
    path("contact",views.contact, name="contact"),

    path("shop/", views.shop, name="shop"),
    path("tshirts/", views.tshirts, name="tshirts"),
    path("tracks/", views.tracks, name="tracks"),
    path("jeans/", views.jeans, name="jeans"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register_page, name="register"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),

]
