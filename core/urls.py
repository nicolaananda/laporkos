from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from tiket import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.ticket_list, name="ticket_list"), 
    path(
        "submit-tiket/", views.submit_ticket, name="submit_ticket"
    ), 
    path(
        "login/", auth_views.LoginView.as_view(), name="login"
    ),  
    path("logout/", auth_views.LogoutView.as_view(), name="logout"), 
]
