from django.urls import path  # type: ignore

from . import views

urlpatterns = [
    path("", views.submit_ticket, name="submit_ticket"),
    path("tickets/", views.ticket_list, name="ticket_list"),
]
