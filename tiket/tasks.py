# tasks.py
import time

from huey.contrib.djhuey import task

from .models import Ticket


@task()
def proses(ticket_id):
    time.sleep(5)

    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.is_active = True
    ticket.save()

    ticket.refresh_from_db()

    print(
        f"[Huey] Tiket '{ticket.title}' (Kamar: {ticket.room_number}) telah diaktifkan setelah delay."
    )
