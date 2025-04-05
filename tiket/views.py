from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import TicketForm
from .models import Ticket
from .tasks import proses 


def ticket_list(request):
    # Get all active tickets
    tickets = Ticket.objects.filter(is_active=True).order_by(
        "-created_at"
    )  

    paginator = Paginator(tickets, 5)  

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "tiket/ticket_list.html", {"page_obj": page_obj})


@login_required
def submit_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.is_active = False
            ticket.save()

            proses(ticket.id)

            return redirect("ticket_list")
    else:
        form = TicketForm()

    return render(request, "tiket/submit_ticket.html", {"form": form})
