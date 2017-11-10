import io

from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from reservations.models import Reservation, Customer

@login_required
def print_ticket(request, reservation_id):
    from pprint import pprint
    pprint(request.user.username)
    details = get_object_or_404(Customer, email=request.user.username)

    ticket = get_object_or_404(Reservation, pk=reservation_id)


    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment;"\
    "filename=%s_%s.pdf" % (
        details.name,
        ticket.destination
        )

    html =render_to_string("reservations/print_ticket.html", {
        "ticket": ticket,
        "details": details,
        "MEDIA_ROOT": settings.MEDIA_ROOT,
        "STATIC_ROOT": settings.STATIC_ROOT,
    })


    pdf = pisa.pisaDocument(io.StringIO(html),response,encoding="UTF-8")

    return response
